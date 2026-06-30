

from keyboards import (
    region_keyboard,
    degree_keyboard,
    funding_keyboard,
    field_keyboard
)

REGIONS = {
    "europe": "Europe",
    "north_america": "North America",
    "asia": "Asia",
    "africa": "Africa",
    "south_america": "South America",
    "australia": "Australia"
}

async def start(update, context):
    await update.message.reply_text(
        "🎓 *Welcome to CKL Scholarship Assistant!*\n\n"
        "Your AI-powered scholarship finder.\n\n"
        "🌍 Choose a region:",
        parse_mode="Markdown",
        reply_markup=region_keyboard(),
    )


async def button_click(update, context):
    query = update.callback_query
    await query.answer()

    if query.data in REGIONS:
        await query.edit_message_text(
            "🎓 Choose a degree:",
            reply_markup=degree_keyboard(),
        )

    elif query.data.startswith("degree_"):
        await query.edit_message_text(
            "💰 Choose a funding option:",
            reply_markup=funding_keyboard(),
        )

    elif query.data.startswith("funding_"):
        await query.edit_message_text(
            "📚 Choose a field of study:",
            reply_markup=field_keyboard(),
        )

    else:
        await query.edit_message_text(
            f"You selected: {query.data}"
        )
