# HerePhishyPhishy
# Eric Holguin
# Mohammad Hossain
# Cyber Infrastructre Defense
# Final Project

from PyInquirer import style_from_dict, Token

APP_KEY = 'c8f772145fcda6fd601595a54c9bc2fcfc8b66bdb860afd1dbba4672646649d5'

BRAND = """
\u001b[35m    __  __ \u001b[36m                          ()
\u001b[35m   / / / /__  ________  \u001b[31:1m                               @/*
\u001b[35m  / /_/ / _ \/ ___/ _ \ \u001b[36m          () \u001b[31:1m               @//////*/@
\u001b[35m / __  /  __/ /  /  __/  \u001b[36m             () \u001b[31:1m         @//////////.
\u001b[35m/_/ /_/\___/_/  _\___/ __ \u001b[36m          () \u001b[31:1m       @*////////*@*///*%
\u001b[35m   / __ \/ /_  (_)____/ /_  __  __ \u001b[31:1m       (@#/**///////////////@
\u001b[35m  / /_/ / __ \/ / ___/ __ \/ / / /      \u001b[37m@@%/\u001b[31:1m/\u001b[37m/*/\u001b[31:1m//\u001b[37m///*/#\u001b[31:1m/////*/@      @*
\u001b[35m / ____/ / / / (__  ) / / / /_/ /     \u001b[37m@    .    (      &\u001b[31:1m///////(#    #//*.
\u001b[35m/_/ __/_/ /_/_/____/_/ /_/\__, / \u001b[36m () \u001b[37m @   %  @      @   /\u001b[31:1m///////@   %/////@
\u001b[35m   / __ \/ /_  (_)____/ //____/ __    \u001b[37m.*%.&,    @      #\u001b[31:1m/////////////(///
\u001b[35m  / /_/ / __ \/ / ___/ __ \/ / / / \u001b[31:1m  @/////\u001b[37m@/**\u001b[31:1m//\u001b[37m/(*/%\u001b[31:1m/////////////////*(
\u001b[35m / ____/ / / / (__  ) / / / /_/ /  \u001b[31:1m &/////////////*#@#//////#*////////#
\u001b[35m/_/   /_/ /_/_/____/_/ /_/\__, /   \u001b[31:1m  ((//////%%//#////////////(  &//*/@
\u001b[35m                         /____/              \u001b[31:1m #*//*&@@@ *////&   *#
                                             \u001b[31:1m   &. .    ,(/,
\u001b[0m
"""

STYLE = style_from_dict({
    Token.QuestionMark: '#fac731 bold',
    Token.Separator: '#cc5454',
    Token.Selected: '#FF1493',  # default
    Token.Pointer: '#4688f1 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '#4688f1 bold',
})