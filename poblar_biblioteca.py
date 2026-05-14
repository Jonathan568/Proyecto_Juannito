import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'universidad_root.settings')
django.setup()

from Biblioteca.models import Libro, LibroFisico

def poblar_biblioteca():
    print("Iniciando carga de libros...")

    libros_data = [
        ("Clean Code", "Robert C. Martin", "9780132350884", "Prentice Hall"),
        ("Introduction to Algorithms", "Thomas H. Cormen", "9780262033848", "MIT Press"),
        ("Django for Beginners", "William S. Vincent", "9781735467702", "WelcomeToCode"),
        ("The Pragmatic Programmer", "Andrew Hunt", "9780135957059", "Addison-Wesley"),
        ("Learning Python", "Mark Lutz", "9781449355739", "O'Reilly Media")
    ]

    for titulo, autor, isbn, editorial in libros_data:
        libro, creado = Libro.objects.get_or_create(
            isbn=isbn,
            defaults={
                'titulo': titulo,
                'autor': autor,
                'editorial': editorial
            }
        )
        
        if creado:
            LibroFisico.objects.create(
                codigo_barras=f"BC-{isbn[:4]}-01",
                estado='disponible',
                idlibro=libro
            )
            LibroFisico.objects.create(
                codigo_barras=f"BC-{isbn[:4]}-02",
                estado='disponible',
                idlibro=libro
            )
            print(f"✅ Libro añadido: {titulo}")
        else:
            print(f"ℹ️ El libro '{titulo}' ya existía.")

    print("\n--- Carga finalizada con éxito ---")

if __name__ == "__main__":
    poblar_biblioteca()