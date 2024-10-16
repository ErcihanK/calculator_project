import os
import importlib
import logging
from commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand, MenuCommand
from config import ENV, API_KEY

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_plugins(commands):
    """Dynamically load command plugins from the 'plugins' folder."""
    plugin_folder = './plugins'
    for file in os.listdir(plugin_folder):
        if file.endswith('.py'):
            module_name = file[:-3]
            module = importlib.import_module(f'plugins.{module_name}')
            command_class = getattr(module, f'{module_name.capitalize()}Command')
            commands[module_name] = command_class()

def print_menu(commands):
    """Logs the available commands."""
    logging.info("\nAvailable commands:")
    for command in commands:
        logging.info(f" - {command}")
    logging.info("\nType 'menu' to see available commands again or 'exit' to quit.")

def main():
    logging.info(f"\nRunning in {ENV} environment")
    logging.info(f"API Key: {API_KEY}")

    commands = {
        'add': AddCommand(),
        'subtract': SubtractCommand(),
        'multiply': MultiplyCommand(),
        'divide': DivideCommand(),
        'menu': MenuCommand(),
    }

    load_plugins(commands)  # Load additional commands from the plugins folder

    logging.info("\nWelcome to the Interactive Calculator!")
    print_menu(commands)

    while True:
        user_input = input("\nEnter command and number(s) (e.g., 'add 1 2', 'square 4'), or 'exit' to quit: ")

        if user_input == 'exit':
            logging.info("Goodbye!")
            break

        try:
            inputs = user_input.split()
            command_name = inputs[0]

            if command_name == 'menu':
                print_menu(commands)
                continue

            if command_name in commands:
                if command_name in ['add', 'subtract', 'multiply', 'divide'] and len(inputs) != 3:
                    raise ValueError(f"{command_name} requires 2 numbers. Usage: {command_name} <num1> <num2>")
                elif command_name not in ['add', 'subtract', 'multiply', 'divide'] and len(inputs) != 2:
                    raise ValueError(f"{command_name} requires 1 number. Usage: {command_name} <num1>")

                # Execute the command
                if len(inputs) == 3:
                    x = float(inputs[1])
                    y = float(inputs[2])
                    result = commands[command_name].execute(x, y)
                else:
                    x = float(inputs[1])
                    result = commands[command_name].execute(x)

                logging.info(f"Result: {result}")
            else:
                logging.error(f"Unknown command: '{command_name}'")

        except ValueError as e:
            logging.error(f"Error: {e}")
        except Exception as e:
            logging.error(f"Invalid input or error: {e}")

if __name__ == "__main__":
    main()
