import os
import importlib
import logging
from commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand, MenuCommand
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)

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
    """Prints the available commands in a user-friendly format."""
    logging.info("\nAvailable commands:")
    for command in commands:
        logging.info(f" - {command}")
    logging.info("\nType 'menu' to see available commands again or 'exit' to quit.")

def main():
    # Access environment variables
    env = os.getenv('ENV')
    api_key = os.getenv('API_KEY')

    # Display the environment information (useful for testing and debugging)
    logging.info(f"Running in {env} environment")
    logging.info(f"API Key: {api_key}")

    commands = {
        'add': AddCommand(),
        'subtract': SubtractCommand(),
        'multiply': MultiplyCommand(),
        'divide': DivideCommand(),
        'menu': MenuCommand(),
    }

    load_plugins(commands)  # Load additional commands from the plugins folder

    logging.info("Welcome to the Interactive Calculator!")
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
                # Handle two-argument commands (e.g., add, subtract, multiply, divide)
                if command_name in ['add', 'subtract', 'multiply', 'divide'] and len(inputs) != 3:
                    raise ValueError(f"{command_name} requires 2 numbers. Usage: {command_name} <num1> <num2>")
                # Handle one-argument commands (e.g., square, cube, sqrt)
                elif command_name not in ['add', 'subtract', 'multiply', 'divide'] and len(inputs) != 2:
                    raise ValueError(f"{command_name} requires 1 number. Usage: {command_name} <num1>")

                # Execute the command
                if len(inputs) == 3:  # Commands that take 2 arguments
                    x = float(inputs[1])
                    y = float(inputs[2])
                    result = commands[command_name].execute(x, y)
                else:  # Commands that take 1 argument
                    x = float(inputs[1])
                    result = commands[command_name].execute(x)

                # Display result and format output
                if isinstance(result, complex):
                    # Display only the real part if the imaginary part is 0
                    if result.imag == 0:
                        logging.info(f"Result: {result.real}")
                    else:
                        logging.info(f"Result: {result}")
                elif isinstance(result, float) and result.is_integer():
                    logging.info(f"Result: {int(result)}")
                else:
                    logging.info(f"Result: {result}")
            else:
                logging.error(f"Unknown command: '{command_name}'")

        except ValueError as e:
            logging.error(f"Error: {e}")
        except Exception as e:
            logging.error(f"Invalid input or error: {e}")


if __name__ == "__main__":
    main()
