from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ParseMode
import sympy as sp

# Replace with your Telegram API key
TOKEN = '8482581885:AAEQ-h0MECtNBcZ76kehgX_a4bd0IC9w7xA'

# Start command
def start(update, context):
    update.message.reply_text('Welcome to MathSolverBot! Use /calc <expression> to solve math problems (e.g., /calc 2+2 or /calc sin(90)). Type /help for more info.')

# Help command
def help_command(update, context):
    update.message.reply_text('Commands:\n/calc <expression> - Solve a math expression\nExamples:\n/calc 2+2\n/calc sin(90)\n/calc 3*x=12\nSupports arithmetic, algebra, trigonometry, and more!')

# Calculate command
def calculate(update, context):
    expression = ' '.join(context.args)  # Get the expression after /calc
    if not expression:
        update.message.reply_text('Please provide an expression (e.g., /calc 2+2).')
        return

    try:
        # Define symbolic variable if needed
        x = sp.Symbol('x')
        # Evaluate the expression
        result = sp.sympify(expression)
        if isinstance(result, sp.Eq):  # Handle equations like 3*x=12
            solution = sp.solve(result, x)
            update.message.reply_text(f'Solution: x = {solution[0]}', parse_mode=ParseMode.MARKDOWN)
        else:
            update.message.reply_text(f'Result: {result.evalf()}', parse_mode=ParseMode.MARKDOWN)
    except Exception as e:
        update.message.reply_text('Error: Invalid expression. Please check your input (e.g., /calc 2+2 or /calc sin(90)).')

def main():
    # Create the Updater and pass it your bot's token
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("calc", calculate))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()