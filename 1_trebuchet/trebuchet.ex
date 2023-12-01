defmodule Trebuchet do
  # is_digit returns true if 1-9
  def is_digit(char_str) do
    <<ascii::utf8>> = char_str
    ascii > 48 and ascii < 58
  end

  def extract_numbers(line) do
    if line === "" do
      ""
    else
      head = String.first(line)
      tail = String.slice(line, 1, String.length(line))

      numbers = %{
        "one" => "1",
        "two" => "2",
        "three" => "3",
        "four" => "4",
        "five" => "5",
        "six" => "6",
        "seven" => "7",
        "eight" => "8",
        "nine" => "9"
      }

      matches =
        numbers
        |> Enum.map(fn {k, _} -> k end)
        |> Enum.filter(fn number ->
          String.slice(line, 0, String.length(number)) === number
        end)

      cond do
        is_digit(head) ->
          head <> extract_numbers(tail)

        length(matches) === 1 ->
          digit = numbers[Enum.at(matches, 0)]

          digit <> extract_numbers(tail)

        true ->
          extract_numbers(tail)
      end
    end
  end

  def take_ends(numbers) do
    first = String.first(numbers)
    last = String.slice(numbers, String.length(numbers) - 1, String.length(numbers))

    first <> last
  end

  def to_integer(number_str) do
    {integer, _} = Integer.parse(number_str)
    integer
  end

  def main do
    {:ok, contents} = File.read("input.txt")

    contents
    |> String.split("\n", trim: true)
    |> Enum.map(fn line -> extract_numbers(line) end)
    # |> Enum.map(fn line -> IO.inspect(line) end)
    |> Enum.map(fn line -> take_ends(line) end)
    |> Enum.map(fn line -> to_integer(line) end)
    |> Enum.sum()
  end
end
