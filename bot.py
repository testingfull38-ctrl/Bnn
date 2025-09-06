from telegram.ext import Application, CommandHandler
from telegram import Update
import sympy as sp

TOKEN = '8482581885:AAEQ-h0MECtNBcZ76kehgX_a4bd0IC9w7xA'

async def start(update: Update, context):
    await update.message.reply_text('Welcome to MathSolverBot! Use /calc <expression> to solve math problems (e.g., /calc 2+2). Type /help for more info.')

async def help_command(update: Update, context):
    await update.message.reply_text('Commands:\n/calc <expression> - Solve a math expression\nExamples:\n/calc 2+2\n/calc sin(90)')

async def calculate(update: Update, context):
    expression = ' '.join(context.args)
    if not expression:
        await update.message.reply_text('Please provide an expression (e.g., /calc 2+2).')
        return
    try:
        x = sp.Symbol('x')
        result = sp.sympify(expression)
        if isinstance(result, sp.Eq):
            solution = sp.solve(result, x)
            await update.message.reply_text(f'Solution: x = {solution[0]}')
        else:
            await update.message.reply_text(f'Result: {result.evalf()}')
    except Exception as e:
        await update.message.reply_text('Error: Invalid expression.')

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("calc", calculate))
    application.run_polling()

if __name__ == '__main__':
    main()
