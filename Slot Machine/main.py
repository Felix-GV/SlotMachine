import random

#Constants

MIN_BET = 1
MAX_LINES = 3
MAX_BET = 1000
ROWS = 3
COLS = 3

symbol_count = {
    "cherry": 2,
    "lemon": 4,
    "orange": 6,
    "plum": 8
}

symbol_value = {
    "cherry": 5,
    "lemon": 4,
    "orange": 3,
    "plum": 2
}


#Functions

def get_slot_machine_results(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    
    return columns 

def get_winnings(columns, lines, bet, value):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                symbol = None
                break
        if symbol is not None:
            winnings += value[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
    
        print()

def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)    
            if amount > 0:
                break
            else: 
                print("Please enter a amount greater than 0.")
        else:
            print("Please enter a number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("How many lines would you like to play? between (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)    
            if 1 <= lines <= MAX_LINES:
                break
            else: 
                print("Enter a valid number of lines")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True:
        bet = input("How much would you like to bet per line? between (1-" + str(MAX_BET) + ")? ")
        if bet.isdigit():
            bet = int(bet)    
            if MIN_BET <= bet <= MAX_BET:
                break
            else: 
                print(f"Enter a valid bet between $1 and ${MAX_BET}")
        else:
            print("Please enter a number.")
    return bet

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if bet * lines > balance:
            print("You do not have enough money to make this bet.")
        else:
            break
    print (f"You are betting ${bet} on {lines} lines. Total be is equal to ${total_bet}")

    slots = get_slot_machine_results(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = get_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}")
    print(f"You won on line:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")  
        answer = input("Press space to enter and q to quit.")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"Your final balance is ${balance}")

main()