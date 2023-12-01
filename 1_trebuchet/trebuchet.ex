defmodule Trebuchet do
  def calibrationValue(line) do
    num_chars = for n <- String.to_charlist(line), n > 47 and n < 58, do: n
    num_str = List.to_string(num_chars)

    first = String.first(num_str)
    last = String.slice(num_str, String.length(num_str) - 1, String.length(num_str))

    {calibration, _} = Integer.parse(first <> last)
    calibration
  end

  def main do
    {:ok, contents} = File.read("input.txt")

    sum =
      contents
      |> String.split("\n", trim: true)
      |> Enum.map(fn line -> calibrationValue(line) end)
      |> Enum.sum()

    IO.puts("Sum: #{sum}")
  end
end
