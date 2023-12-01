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

    # >, <, <=, >= are as usual
    age = 16
    IO.puts("Vote & Drive: #{age >= 16 and age >= 18}")
    IO.puts(not true)
  end

  def branching do
    age = 16

    if age >= 18 do
      IO.puts("Can vote")
    else
      IO.puts("Can't vote")
    end

    unless age === 18 do
      IO.puts("Not 18")
    else
      IO.puts("Is 18")
    end

    # like a big if, else if, ...
    cond do
      age >= 18 -> IO.puts("You can vote")
      age >= 16 -> IO.puts("You can drive")
      age >= 14 -> IO.puts("You need to wait")
      true -> IO.puts("Default")
    end

    # like a switch statement
    case 2 do
      1 -> IO.puts("One")
      2 -> IO.puts("Two")
      _ -> IO.puts("Default")
    end

    IO.puts("Ternary: #{if age > 18, do: "Can vote", else: "Can't vote"}")
  end

  def tuples do
    # normally contain 2-4 values. not for enumeration (looping)
    my_stats = {175, 6.25, :MyAtom}

    IO.puts("Tuple?: #{is_tuple(my_stats)}")

    # all variables are constant
    my_stats2 = Tuple.append(my_stats, 42)

    IO.puts("Age: #{elem(my_stats2, 3)}")

    IO.puts("Size: #{tuple_size(my_stats2)}")

    my_stats3 = Tuple.delete_at(my_stats2, 0)

    my_stats4 = Tuple.insert_at(my_stats3, 0, 1974)
    IO.puts("Mutated: #{Enum.join(my_stats4)}")

    many_zeroes = Tuple.duplicate(0, 5)

    {weight, height, name} = {175, 6.25, "MyAtom"}
    IO.puts("Weight: #{weight}")
  end
end
