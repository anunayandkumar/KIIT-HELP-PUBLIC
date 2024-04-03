from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


from KIIT_Student_Bot import jobs,openaiprompt,sgpaCalculator
from MachineLearning_Predictions import salaryPrediction,placementPrediction
from KIIT_HELP import kiit
from Fun_API import film_movie,getjoke,lovepercent

def main():
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(f"Hello . Welcome to KIIT HELP . Enter /help to explore accepted commands .")

    async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        help_message = f"You can access the features using the following commands:\n\n"
        help_message = help_message + f"1. /start : Starts the bot .\n\n"
        help_message = help_message + f"2. /help : Help Command. \n\n"
        help_message = help_message + f"3. /get_timetable: Access Personalized Time Table.\n\n"
        help_message = help_message + f"4. /sgpa : Calculates SGPA . \nFormat : /sgpa grade_point_in_sub1 sub1Credit /sgpa grade_point_in_sub2 sub2Credit. \nEx : /sgpa 8 3 9 3 8 4 and so on till all subjects are covered"
        help_message = help_message + f"5. /chat : Enter Command followed by prompt to get any help . Ex : /chat Describe Bhubaneshwar. \n\n"
        help_message = help_message + f"6. /placements : Enter command followed by argument . Ex : /placements arg1 arg2 arg 3 and so on.. \n\n"
        help_message = help_message + f"7. /salary : Enter command followed by argument . Ex : /salary arg1 arg2 arg 3 and so on.. \n\n"
        help_message = help_message + f"8. /job : Enter Command followed by Job Title . Ex: /job Web Developer. \n\n"
        help_message = help_message + f"9. /fun : Explore Some Fun Features"


        await update.message.reply_text(help_message)

    async def get_timetable(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        get_timetable_message = f"To get your today's Time table , \nEnter : /timetable <your roll number>. \n\n"
        get_timetable_message = get_timetable_message + f"For example your roll number is 21052142 . Your message should be /timetable 21052142 . \n"
        await update.message.reply_text(get_timetable_message)

    async def timetable(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        roll = int(context.args[0])
        finalString = kiit.result(roll)
        await update.message.reply_text(finalString)

    async def sgpa(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        ans = sgpaCalculator.get_sgpa(context.args)
        ans = format(ans, '.2f')
        await update.message.reply_text(f"Your SGPA is : " + str(ans))



    async def job(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        title = " ".join(context.args)
        final =jobs.jobSearch(title)
        finalString1 = final[0]
        finalString2 = final[1]
        finalString3 = final[2]
        await update.message.reply_text(finalString1)
        await update.message.reply_text(finalString2)
        await update.message.reply_text(finalString3)

    async def placements(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        v1 = context.args[0]
        v2 = float(context.args[1])
        v3 = context.args[2]
        v4 = float(context.args[3])
        v5 = context.args[4]
        v6 = context.args[5]
        v7 = float(context.args[6])
        v8 = context.args[7]
        v9 = context.args[8]
        v10 = float(context.args[9])
        v11 = context.args[10]
        v12 = float(context.args[11])
        placementFlag = placementPrediction.placement(v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12)
        arr = int(placementFlag[0])
        if arr==1:
            await update.message.reply_text("You will be placed successfully.")
        else:
            await update.message.reply_text("You will not be placed . You need to work harder .")


    async def salary(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        v1 = float(context.args[0])
        v2 = float(context.args[1])
        v3 = float(context.args[2])
        v4 = float(context.args[3])
        v5 = float(context.args[4])
        v6 = float(context.args[5])
        v7 = float(context.args[6])
        v8 = float(context.args[7])
        v9 = float(context.args[8])
        v10 = float(context.args[9])
        v11 = float(context.args[10])
        v12 = float(context.args[11])
        v13 = float(context.args[12])
        v14 = float(context.args[13])
        v15 = float(context.args[14])
        v16 = float(context.args[15])
        v17 = float(context.args[16])
        v18 = float(context.args[17])
        v19 = float(context.args[18])
        v20 = float(context.args[19])
        v21 = float(context.args[20])
        v22 = float(context.args[21])
        finalSalary = salaryPrediction.predictSalary(v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22)
        await update.message.reply_text(f"Your salary will be Rs. : "+str(finalSalary))


    async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        prompt = " ".join(context.args)
        generated_query = openaiprompt.generate_text(prompt)
        await update.message.reply_text(generated_query)

    async def fun(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        funHelp = "The following Fun Features are Available Now ."
        funHelp = funHelp + f"/love . Calculate Love Percentage among Friends . Ex : /love Ayush Priyanka.\n\n"
        funHelp = funHelp + f"/jokes. Get access to Random Jokes\n\n"
        funHelp = funHelp + (f"/movieseries . Get list of movies and Web Series of your favourite genre from start to end year ."
                             f"Ex: /movieseries Drama 2002 2020 3 , where 2002 is start year and 2020 is end year & 3 being the number of result you require")
        await update.message.reply_text(funHelp)


    async def movieseries(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        g = context.args[0]
        s = int(context.args[1])
        e = int(context.args[2])
        n = int(context.args[3])
        movser = film_movie.mov(g,s,e,n)
        for i in range(n):
            await update.message.reply_text(movser[i])

    async def love(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        sname = context.args[0]
        fname = context.args[1]
        result = lovepercent.love(sname, fname)
        await update.message.reply_text(result)

    async def jokes(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        result = getjoke.getjokes()
        await update.message.reply_text(result)

    app = ApplicationBuilder().token("TOKEN").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("get_timetable", get_timetable))
    app.add_handler(CommandHandler("sgpa", sgpa))

    app.add_handler(CommandHandler("timetable", timetable))
    app.add_handler(CommandHandler("placements", placements))
    app.add_handler(CommandHandler("salary", salary))
    app.add_handler(CommandHandler("job", job))
    app.add_handler(CommandHandler("fun", fun))
    app.add_handler(CommandHandler("love", love))
    app.add_handler(CommandHandler("jokes", jokes))
    app.add_handler(CommandHandler("movieseries", movieseries))
    app.add_handler(CommandHandler("chat", chat))





    app.run_polling()


if __name__ == "__main__":
    main()
