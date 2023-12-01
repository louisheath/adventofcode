defmodule Trebuchet do
  def fixNumbers(line) do
    if line === "" do
      ""
    else
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

      if length(matches) === 1 do
        number = Enum.at(matches, 0)
        digit = numbers[number]

        # clean the remainder
        digit <>
          fixNumbers(String.slice(line, String.length(number), String.length(line)))
      else
        # there's no number starting here. check the rest
        String.slice(line, 0, 1) <> fixNumbers(String.slice(line, 1, String.length(line)))
      end
    end
  end

  def calibrate(line) do
    num_chars = for n <- String.to_charlist(line), n > 48 and n < 58, do: n
    num_str = List.to_string(num_chars)

    first = String.first(num_str)
    last = String.slice(num_str, String.length(num_str) - 1, String.length(num_str))

    {calibration, _} = Integer.parse(first <> last)
    calibration
  end

  def main do
    {:ok, contents} = File.read("input3.txt")

    contents
    |> String.split("\n", trim: true)
    |> Enum.map(fn line -> fixNumbers(line) end)
    |> Enum.map(fn line -> calibrate(line) end)
    # |> Enum.map(fn line -> IO.inspect(line) end)
    |> Enum.sum()
  end
end
