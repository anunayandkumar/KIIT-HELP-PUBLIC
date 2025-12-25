import os
import asyncio
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

# --- Your internal modules ---
from KIIT_Student_Bot import jobs, openaiprompt, sgpaCalculator
from MachineLearning_Predictions import salaryPrediction, placementPrediction
from KIIT_HELP import kiit
from Fun_API import film_movie, getjoke, lovepercent


# ---------------- COMMANDS ---------------- #

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello 👋 Welcome to KIIT HELP.\nEnter /help to explore commands."
    )


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_message = (
        "Available Commands:\n\n"
        "/start - Start the bot\n"
        "/help - Show this help\n"
        "/get_timetable - How to get timetable\n"
        "/timetable <roll_no>\n"
        "/sgpa <grade credit grade credit ...>\n"
        "/job <job title>\n"
        "/chat <prompt>\n"
        "/placements <args...>\n"
        "/salary <args...>\n"
        "/fun - Fun commands\n"
        "/love <name1> <name2>\n"
        "/jokes\n"
        "/movieseries <genre> <start_year> <end_year> <count>"
    )
    await update.message.reply_text(help_message)


async def get_timetable(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Usage:\n/timetable <roll_number>\nExample:\n/timetable 21052142"
    )


async def timetable(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 1:
        await update.message.reply_text("Usage: /timetable <roll_number>")
        return

    try:
        roll = int(context.args[0])
        result = kiit.result(roll)
        await update.message.reply_text(result)
    except Exception:
        await update.message.reply_text("Invalid roll number.")


async def sgpa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /sgpa <grade credit grade credit ...>")
        return

    try:
        ans = sgpaCalculator.get_sgpa(context.args)
        await update.message.reply_text(f"Your SGPA is: {ans:.2f}")
    except Exception:
        await update.message.reply_text("Invalid SGPA input format.")


async def job(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /job <job title>")
        return

    title = " ".join(context.args)

    try:
        # Run blocking code safely
        final = await asyncio.to_thread(jobs.jobSearch, title)

        if not final:
            await update.message.reply_text("No jobs found.")
            return

        for item in final[:3]:
            await update.message.reply_text(str(item))

    except Exception as e:
        print("JOB ERROR:", e)
        await update.message.reply_text("Failed to fetch jobs.")


async def placements(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 12:
        await update.message.reply_text("Invalid number of arguments for /placements")
        return

    try:
        args = context.args
        result = placementPrediction.placement(
            args[0], float(args[1]), args[2], float(args[3]),
            args[4], args[5], float(args[6]), args[7],
            args[8], float(args[9]), args[10], float(args[11])
        )

        if int(result[0]) == 1:
            await update.message.reply_text("You will be placed successfully 🎉")
        else:
            await update.message.reply_text("Placement unlikely. Keep improving 💪")

    except Exception:
        await update.message.reply_text("Error processing placement prediction.")


async def salary(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 22:
        await update.message.reply_text("Invalid number of arguments for /salary")
        return

    try:
        values = list(map(float, context.args))
        final_salary = salaryPrediction.predictSalary(*values)
        await update.message.reply_text(f"Predicted Salary: ₹{final_salary}")

    except Exception:
        await update.message.reply_text("Error calculating salary.")


async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /chat <your question>")
        return

    prompt = " ".join(context.args)

    try:
        response = await asyncio.to_thread(openaiprompt.generate_text, prompt)
        await update.message.reply_text(response)
    except Exception:
        await update.message.reply_text("AI service unavailable.")


async def fun(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/love <name1> <name2>\n"
        "/jokes\n"
        "/movieseries <genre> <start_year> <end_year> <count>"
    )


async def movieseries(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 4:
        await update.message.reply_text("Usage: /movieseries <genre> <start> <end> <count>")
        return

    try:
        g, s, e, n = context.args[0], int(context.args[1]), int(context.args[2]), int(context.args[3])
        result = film_movie.mov(g, s, e, n)
        for item in result[:n]:
            await update.message.reply_text(item)
    except Exception:
        await update.message.reply_text("Error fetching movies.")


async def love(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 2:
        await update.message.reply_text("Usage: /love <name1> <name2>")
        return

    result = lovepercent.love(context.args[0], context.args[1])
    await update.message.reply_text(result)


async def jokes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    joke = getjoke.getjokes()
    await update.message.reply_text(joke)


# ---------------- ERROR HANDLER ---------------- #

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("GLOBAL ERROR:", context.error)
    if update and update.message:
        await update.message.reply_text("⚠️ Something went wrong.")


# ---------------- MAIN ---------------- #

def main():
    TOKEN = ""
    if not TOKEN:
        raise RuntimeError("TELEGRAM_BOT_TOKEN not set")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("get_timetable", get_timetable))
    app.add_handler(CommandHandler("timetable", timetable))
    app.add_handler(CommandHandler("sgpa", sgpa))
    app.add_handler(CommandHandler("job", job))
    app.add_handler(CommandHandler("placements", placements))
    app.add_handler(CommandHandler("salary", salary))
    app.add_handler(CommandHandler("chat", chat))
    app.add_handler(CommandHandler("fun", fun))
    app.add_handler(CommandHandler("love", love))
    app.add_handler(CommandHandler("jokes", jokes))
    app.add_handler(CommandHandler("movieseries", movieseries))

    app.add_error_handler(error_handler)

    print("🤖 Bot started...")
    app.run_polling()


if __name__ == "__main__":
    main()

