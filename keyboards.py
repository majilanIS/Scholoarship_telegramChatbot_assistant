from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# button for region selection
def region_keyboard():
    keyboard = [
        [InlineKeyboardButton("🇪🇺 Europe", callback_data="europe")],
        [InlineKeyboardButton("🌎 North America", callback_data="north_america")],
        [InlineKeyboardButton("🌏 Asia", callback_data="asia")],
        [InlineKeyboardButton("🌍 Africa", callback_data="africa")],
        [InlineKeyboardButton("🌎 South America", callback_data="south_america")],
        [InlineKeyboardButton("🇦🇺 Australia", callback_data="australia")]
    ]

    return InlineKeyboardMarkup(keyboard)

# button for degree selection
def degree_keyboard():
    keyboard = [
        [InlineKeyboardButton("🎓 Bachelor's", callback_data="degree_bachelor")],
        [InlineKeyboardButton("🎓 Master's", callback_data="degree_master")],
        [InlineKeyboardButton("🎓 PhD", callback_data="degree_phd")],
        [InlineKeyboardButton("🎯 Any", callback_data="degree_any")]
    ]

    return InlineKeyboardMarkup(keyboard)

# button for funding selection
def funding_keyboard():
    keyboard = [
        [InlineKeyboardButton("💰 Fully Funded", callback_data="funding_full")],
        [InlineKeyboardButton("💵 Partial", callback_data="funding_partial")],
        [InlineKeyboardButton("🎯 Any", callback_data="funding_any")]
    ]

    return InlineKeyboardMarkup(keyboard)

# button for field of study selection
def field_keyboard():
    keyboard = [
        [InlineKeyboardButton("💻 Computer Science", callback_data="field_cs")],
        [InlineKeyboardButton("🔐 Cybersecurity", callback_data="field_cyber")],
        [InlineKeyboardButton("🤖 Artificial Intelligence", callback_data="field_ai")],
        [InlineKeyboardButton("📊 Data Science", callback_data="field_ds")],
        [InlineKeyboardButton("⚙ Engineering", callback_data="field_engineering")],
        [InlineKeyboardButton("📚 Business", callback_data="field_business")]
    ]

    return InlineKeyboardMarkup(keyboard)