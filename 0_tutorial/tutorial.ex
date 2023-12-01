defmodule Tutorial do
  def main do
    name = IO.gets("What is your name? ") |> String.trim()
    IO.puts("Hello #{name}")
  end

  def types do
    my_int = 123
    IO.puts("Integer: #{is_integer(my_int)}")
    IO.puts("Float: #{is_float(my_int)}")

    # wtf is an atom
    IO.puts("Atom #{is_atom(:Hello)}")

    # range
    one_to_10 = 1..10

    my_str = "My sentence"
    IO.puts("Length #{String.length(my_str)}")

    # === checks value and data type
    IO.puts("Equal: #{"Egg" === "egg"}")

    # string things
    longer_str = my_str <> " " <> "is now longer"
    IO.puts("My ? #{String.contains?(longer_str, "My")}")
    IO.puts("First: #{String.first(my_str)}")
    IO.puts("Index 4: #{String.at(my_str, 4)}")
    IO.puts("Substring: #{String.slice(my_str, 3, 8)}")

    IO.inspect(String.split(my_str, " "))
    IO.puts(String.reverse(longer_str))
    IO.puts(String.upcase(longer_str))

    # pipe
    (4 * 10) |> IO.puts()

    # arithmetic. -, * also as expected
    IO.puts("5 + 4: #{5 + 4}")
    # / yields a float
    IO.puts("5 / 4: #{5 / 4}")
    # modulus
    IO.puts("5 div 4: #{div(5, 4)}")
    # remainder
    IO.puts("5 rem 4: #{rem(5, 4)}")

    IO.puts("4 == 4.0: #{4 == 4.0}")
    IO.puts("4 === 4.0: #{4 === 4.0}")
    IO.puts("4 != 4.0: #{4 != 4.0}")
    IO.puts("4 !== 4.0: #{4 !== 4.0}")
  end
end
