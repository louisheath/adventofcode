defmodule Trebuchet do
  def extractDigits(line) do
    1
  end

  def main do
    {:ok, contents} = File.read("input.txt")

    sum =
      contents
      |> String.split("\n", trim: true)
      |> Enum.map(fn line -> 1 end)
      |> Enum.sum()

    IO.puts("Sum: #{sum}")
  end
end
