import argparse

from scripts import command_generate, command_copy, command_cargo

def command_all():
    command_generate()
    command_copy()
    command_cargo()

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--libcheck-path", type=str)
    subparsers = parser.add_subparsers(help='sub-command help')

    parser_generate = subparsers.add_parser(
        'generate', help='generate updated problems')
    parser_generate.set_defaults(func=command_generate)

    parser_copy = subparsers.add_parser('copy', help='copy problems')
    parser_copy.set_defaults(func=command_copy)

    parser_cargo = subparsers.add_parser('cargo', help='update cargo.toml')
    parser_cargo.set_defaults(func=command_cargo)
    
    parser_all = subparsers.add_parser('all', help='all')
    parser_all.set_defaults(func=command_all)

    args = parser.parse_args()

    args.func()
