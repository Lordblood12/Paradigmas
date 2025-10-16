
import json
from typing import List, Optional, Dict, Any
from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict, field
import os

# -----------------------
# Modelos / Clases
# -----------------------

class Item(ABC):
    """Clase abstracta para un ítem de biblioteca (libro, revista...)."""
    def __init__(self, id: int, title: str, author: str, publication_year: int, quantity: int):
        self._id = int(id)                  # encapsulamiento (atributo 'privado')
        self._title = title
        self._author = author
        self._publication_year = int(publication_year)
        self._quantity = int(quantity)

    @property
    def id(self) -> int:
        return self._id

    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> str:
        return self._author

    @property
    def publication_year(self) -> int:
        return self._publication_year

    @property
    def quantity(self) -> int:
        return self._quantity

    def decrease_quantity(self, amount: int = 1) -> bool:
        if self._quantity >= amount:
            self._quantity -= amount
            return True
        return False

    def increase_quantity(self, amount: int = 1):
        self._quantity += amount

    @abstractmethod
    def type_name(self) -> str:
        """Para polimorfismo: cada subclase devuelve su tipo (Libro, Revista, ...)"""
        pass

    def to_dict(self) -> Dict[str, Any]:
        """Serializa propiedades comunes; subclases añadirán sus campos"""
        return {
            "class": self.__class__.__name__,
            "id": self._id,
            "title": self._title,
            "author": self._author,
            "publication_year": self._publication_year,
            "quantity": self._quantity
        }

    def __str__(self) -> str:
        return f"[{self.type_name()}] ID:{self._id} - '{self._title}' por {self._author} ({self._publication_year}) - Cantidad: {self._quantity}"


class Book(Item):
    """Libro — ejemplo de herencia de Item."""
    def __init__(self, id: int, title: str, author: str, publication_year: int, genre: str, quantity: int):
        super().__init__(id, title, author, publication_year, quantity)
        self._genre = genre

    @property
    def genre(self) -> str:
        return self._genre

    def type_name(self) -> str:
        return "Libro"

    def to_dict(self) -> Dict[str, Any]:
        d = super().to_dict()
        d.update({"genre": self._genre})
        return d


class Magazine(Item):
    """Revista — otra subclase; demuestra polimorfismo."""
    def __init__(self, id: int, title: str, editor: str, publication_year: int, issue_number: int, quantity: int):
        super().__init__(id, title, editor, publication_year, quantity)
        self._issue_number = int(issue_number)

    @property
    def issue_number(self) -> int:
        return self._issue_number

    def type_name(self) -> str:
        return "Revista"

    def to_dict(self) -> Dict[str, Any]:
        d = super().to_dict()
        d.update({"issue_number": self._issue_number})
        return d


class Member:
    """Representa a un usuario/miembro de la biblioteca."""
    def __init__(self, id: int, name: str):
        self._id = int(id)
        self._name = name
        self._issued_books: List[int] = []  # almacena IDs de items prestados

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def issued_books(self) -> List[int]:
        return list(self._issued_books)  # retornamos copia (encapsulamiento)

    def issue(self, item_id: int):
        self._issued_books.append(int(item_id))

    def return_item(self, item_id: int) -> bool:
        try:
            self._issued_books.remove(int(item_id))
            return True
        except ValueError:
            return False

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self._id,
            "name": self._name,
            "issued_books": list(self._issued_books)
        }

    def __str__(self) -> str:
        return f"Miembro ID:{self._id} - {self._name} - Libros prestados: {len(self._issued_books)}"


# -----------------------
# Biblioteca (Facade / Agregación)
# -----------------------

class Library:
    """Abstrae el conjunto de items y miembros y proporciona operaciones."""
    def __init__(self, items: Optional[List[Item]] = None, members: Optional[List[Member]] = None):
        self._items: Dict[int, Item] = {item.id: item for item in (items or [])}
        self._members: Dict[int, Member] = {m.id: m for m in (members or [])}

    # --- gestión de items
    def add_item(self, item: Item):
        if item.id in self._items:
            # si existe, sumamos cantidad (comportamiento simple)
            self._items[item.id].increase_quantity(item.quantity)
        else:
            self._items[item.id] = item

    def find_item_by_id(self, item_id: int) -> Optional[Item]:
        return self._items.get(int(item_id))

    def search_items(self, term: str) -> List[Item]:
        term_lower = term.lower()
        return [i for i in self._items.values()
                if term_lower in i.title.lower() or term_lower in i.author.lower()]

    def list_items(self) -> List[Item]:
        return list(self._items.values())

    # --- gestión de miembros
    def add_member(self, member: Member):
        if member.id in self._members:
            raise ValueError(f"Miembro con ID {member.id} ya existe.")
        self._members[member.id] = member

    def find_member_by_id(self, member_id: int) -> Optional[Member]:
        return self._members.get(int(member_id))

    def list_members(self) -> List[Member]:
        return list(self._members.values())

    # --- préstamos / devoluciones
    def issue_item(self, member_id: int, item_id: int) -> bool:
        member = self.find_member_by_id(member_id)
        item = self.find_item_by_id(item_id)
        if not member or not item:
            return False
        if item.decrease_quantity(1):
            member.issue(item_id)
            return True
        return False

    def return_item(self, member_id: int, item_id: int) -> bool:
        member = self.find_member_by_id(member_id)
        item = self.find_item_by_id(item_id)
        if not member or not item:
            return False
        if member.return_item(item_id):
            item.increase_quantity(1)
            return True
        return False

    # --- persistencia
    def to_json(self) -> Dict[str, Any]:
        return {
            "items": [i.to_dict() for i in self._items.values()],
            "members": [m.to_dict() for m in self._members.values()]
        }

    @classmethod
    def from_json(cls, data: Dict[str, Any]):
        items = []
        for it in data.get("items", []):
            clsname = it.get("class", "Book")
            if clsname == "Book":
                item = Book(it["id"], it["title"], it["author"], it["publication_year"], it.get("genre", "Otro"), it["quantity"])
            elif clsname == "Magazine":
                item = Magazine(it["id"], it["title"], it["author"], it["publication_year"], it.get("issue_number", 0), it["quantity"])
            else:
                # Fallback: crear Book genérico
                item = Book(it["id"], it["title"], it["author"], it["publication_year"], it.get("genre", "Otro"), it["quantity"])
            items.append(item)
        members = []
        for md in data.get("members", []):
            m = Member(md["id"], md["name"])
            for bid in md.get("issued_books", []):
                m.issue(bid)
            members.append(m)
        return cls(items=items, members=members)

    def save_to_files(self, items_file: str = "library.json", members_file: str = "members.json"):
        # Guardamos por separado para facilitar edición manual si se desea
        with open(items_file, "w", encoding="utf-8") as f:
            json.dump([i.to_dict() for i in self._items.values()], f, indent=2, ensure_ascii=False)
        with open(members_file, "w", encoding="utf-8") as f:
            json.dump([m.to_dict() for m in self._members.values()], f, indent=2, ensure_ascii=False)

    @classmethod
    def load_from_files(cls, items_file: str = "library.json", members_file: str = "members.json"):
        def load_list(path):
            if os.path.exists(path):
                with open(path, "r", encoding="utf-8") as f:
                    return json.load(f)
            return []
        items_data = load_list(items_file)
        members_data = load_list(members_file)
        data = {"items": items_data, "members": members_data}
        return cls.from_json(data)


# -----------------------
# Interfaz de consola (menú)
# -----------------------

def prompt_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Entrada no válida. Ingresa un número entero.")

def prompt_nonempty(prompt: str) -> str:
    while True:
        s = input(prompt).strip()
        if s:
            return s
        print("Valor requerido.")

def menu_loop():
    lib = Library.load_from_files()
    print("Biblioteca cargada. Ítems:", len(lib.list_items()), "Miembros:", len(lib.list_members()))
    while True:
        print("\n--- Menú de Biblioteca ---")
        print("1) Agregar libro")
        print("2) Agregar revista")
        print("3) Mostrar ítems")
        print("4) Buscar ítems por término (titulo/autor)")
        print("5) Agregar miembro")
        print("6) Mostrar miembros")
        print("7) Prestar ítem")
        print("8) Devolver ítem")
        print("9) Guardar")
        print("0) Guardar y salir")
        opt = input("Opción: ").strip()
        if opt == "1":
            id_ = prompt_int("ID del libro: ")
            title = prompt_nonempty("Título: ")
            author = prompt_nonempty("Autor: ")
            year = prompt_int("Año publicación: ")
            genre = prompt_nonempty("Género: ")
            qty = prompt_int("Cantidad: ")
            b = Book(id_, title, author, year, genre, qty)
            lib.add_item(b)
            print("Libro agregado.")
        elif opt == "2":
            id_ = prompt_int("ID revista: ")
            title = prompt_nonempty("Título: ")
            editor = prompt_nonempty("Editor: ")
            year = prompt_int("Año publicación: ")
            issue = prompt_int("Número de edición: ")
            qty = prompt_int("Cantidad: ")
            r = Magazine(id_, title, editor, year, issue, qty)
            lib.add_item(r)
            print("Revista agregada.")
        elif opt == "3":
            items = lib.list_items()
            if not items:
                print("No hay ítems.")
            for it in items:
                print(it)
        elif opt == "4":
            term = prompt_nonempty("Término de búsqueda: ")
            found = lib.search_items(term)
            if not found:
                print("No se encontró ninguno.")
            for it in found:
                print(it)
        elif opt == "5":
            id_ = prompt_int("ID miembro: ")
            name = prompt_nonempty("Nombre: ")
            try:
                m = Member(id_, name)
                lib.add_member(m)
                print("Miembro agregado.")
            except ValueError as e:
                print("Error:", e)
        elif opt == "6":
            members = lib.list_members()
            if not members:
                print("No hay miembros.")
            for m in members:
                print(m)
                if m.issued_books:
                    for bid in m.issued_books:
                        item = lib.find_item_by_id(bid)
                        if item:
                            print("  ->", item)
        elif opt == "7":
            mid = prompt_int("ID miembro: ")
            iid = prompt_int("ID ítem a prestar: ")
            ok = lib.issue_item(mid, iid)
            if ok:
                print("Préstamo registrado.")
            else:
                print("No fue posible prestar (miembro/ítem no existe o no hay cantidad).")
        elif opt == "8":
            mid = prompt_int("ID miembro: ")
            iid = prompt_int("ID ítem a devolver: ")
            ok = lib.return_item(mid, iid)
            if ok:
                print("Devolución registrada.")
            else:
                print("No fue posible devolver (miembro/ítem no existe o miembro no tenía ese ítem).")
        elif opt == "9":
            lib.save_to_files()
            print("Guardado.")
        elif opt == "0":
            lib.save_to_files()
            print("Guardado. Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu_loop()
