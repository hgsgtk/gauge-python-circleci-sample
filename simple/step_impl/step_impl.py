from getgauge.python import step, before_scenario, Messages

vowels = ["a", "e", "i", "o", "u"]


def number_of_vowels(word):
    return len([elem for elem in list(word) if elem in vowels])


# --------------------------
# Gauge step implementations
# --------------------------

@step("The word <word> has <number> vowels.")
def assert_no_of_vowels_in(word, number):
    assert str(number) == str(number_of_vowels(word))


@step("Vowels in English language are <vowels>.")
def assert_default_vowels(given_vowels):
    Messages.write_message("Given vowels are {0}".format(given_vowels))
    assert given_vowels == "".join(vowels)

@step("Contexts step を実行する")
def contexts_step_1():
    assert True

@step("Step を実行する")
def exec_step():
    assert True

@step("パラメータ <param> を渡して、Step を実行する")
def exec_step_with_param(param):
    assert param == 'param1'
@step("Almost all words have vowels <table>")
def assert_words_vowel_count(table):
    actual = [str(number_of_vowels(word)) for word in table.get_column_values_with_name("Word")]
    expected = [str(count) for count in table.get_column_values_with_name("Vowel Count")]
    assert expected == actual

@step("Table driven scenario テストを実行する <table>")
def table_driven_1(table):
    actual = [str(number_of_vowels(word)) for word in table.get_column_values_with_name("Word")]
    expected = [str(count) for count in table.get_column_values_with_name("Vowel Count")]
    assert expected == actual

@step("TearDown を実行")
def tear_down_1():
    assert True


# ---------------
# Execution Hooks
# ---------------

@before_scenario()
def before_scenario_hook():
    assert "".join(vowels) == "aeiou"
