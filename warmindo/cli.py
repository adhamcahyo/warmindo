import argparse

def start_project(args):
    project_name = args.project_name
    print(f"Memulai proyek {project_name}...")
    print("Proyek telah berhasil dibuat!")
    print("Oke musik ... selamat coding!")

def migrate(args):
    print("Migrasi basis data...")

def main():
    parser = argparse.ArgumentParser(description="Warmindo CLI")
    subparsers = parser.add_subparsers()

    start_project_parser = subparsers.add_parser('start', help='Mulai proyek baru')
    start_project_parser.add_argument('project_name', type=str, help='Nama proyek')
    start_project_parser.set_defaults(func=start_project)

    migrate_parser = subparsers.add_parser('migrate', help='Migrasi basis data')
    migrate_parser.set_defaults(func=migrate)

    args = parser.parse_args()
    args.func(args)