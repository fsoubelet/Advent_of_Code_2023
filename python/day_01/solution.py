"""
--- Day 1: Trebuchet?! ---

Something is wrong with global snow production, and you've been selected to take a look.
The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

Collect stars by solving puzzles.
Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first.
Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills.
Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover.
On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?


--- Part Two ---

Your calculation isn't quite right.
It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line.
For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76.
Adding these together produces 281.

What is the sum of all of the calibration values?
"""
from pathlib import Path

WORDS_TO_DIGITS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def combine_line_first_last_digits_part_1(line: str) -> float:
    """
    Combine the first and last digits of the line.
    Returns the corresponding number when combining the two digits.
    """
    first_digit = None
    last_digit = None
    for element in line:
        if element.isdigit():
            first_digit = element
            break
    for element in reversed(line):
        if element.isdigit():
            last_digit = element
            break
    return int(first_digit + last_digit)


def find_digit_including_words(line: str, reverse: bool = False) -> str:
    """
    Looks either in order or in reverse and gives the first (or corresponding to last, if in reverse)
    digit encountered, be it a word or an actual digit. It is returned as a string.
    """
    word_text = ""
    string_to_check = line[::-1] if reverse else line

    for element in string_to_check:
        # If we find a digit, it's done
        if element.isdigit():
            return element
        # Otherwise we add the letter to the current "word" and will check if this word corresponds to a digit
        word_text += element
        for word in WORDS_TO_DIGITS:
            check = word[::-1] if reverse else word
            if check in word_text:
                return WORDS_TO_DIGITS[word]


def combine_line_first_last_digits_part_2(line: str) -> float:
    """
    Combine the first and last digits of the line, but digits spelled as words are also valid.
    Returns the corresponding number when combining the two digits.
    """
    first_digit = find_digit_including_words(line)
    last_digit = find_digit_including_words(line, reverse=True)
    return int(first_digit + last_digit)


if __name__ == "__main__":
    inputs = Path("input.txt").read_text().splitlines()
    # Part 1
    combined_digits_as_numbers = [combine_line_first_last_digits_part_1(line) for line in inputs]
    print(f"Part 1 answer: {sum(combined_digits_as_numbers)}")

    # Part 2
    combined_digits_as_numbers = [combine_line_first_last_digits_part_2(line) for line in inputs]
    print(f"Part 2 answer: {sum(combined_digits_as_numbers)}")
