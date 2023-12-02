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
    IO.puts("Size: #{tuple_size(my_stats2)}")

    many_zeroes = Tuple.duplicate(0, 5)

    {weight, height, name} = {175, 6.25, "MyAtom"}
    IO.puts("Weight: #{weight}")
  end

  def lists do
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]

    list3 = list1 ++ list2

    list4 = list3 -- list1

    IO.puts(6 in list4)

    [head | tail] = list3
    IO.puts("Head: #{head}")

    # no newline
    IO.write("Tail: ")

    IO.inspect(tail)

    Enum.each(tail, fn item -> IO.puts(item) end)

    words = ["Random", "Words", "in a", "list"]
    Enum.each(words, fn word -> IO.puts(word) end)

    recursive(words)
    recursive(List.delete(words, "Random"))
    recursive(List.delete_at(words, 1))

    # list of key value tuple. like a map?
    my_stats = [name: "Louis", height: 182]
    IO.puts(my_stats[:name])
  end

  def recursive([word | words]) do
    IO.puts(word)
    recursive(words)
  end

  def recursive([]), do: nil

  def maps do
    capitals = %{"Alabama" => "Montgomery", "Alaska" => "Juneau", "Arizona" => "Phoenix"}

    IO.puts("Capital of Alaska is #{capitals["Alaska"]}")

    # using atoms
    capitals2 = %{alabama: "Montgomery", alaska: "Juneau", arizona: "Phoenix"}

    IO.puts("Capital of Arizona is #{capitals2.arizona}")

    capitals3 = Dict.put_new(capitals, "Arkansas", "Little Rock")
  end

  def pattern_matching do
    # retrieve data from different types of data structures
    [length, width] = [20, 30]
    IO.puts("Width: #{width}")

    [_, [_, a]] = [20, [30, 40]]
    IO.puts("Useless number: #{a}")
  end

  def anon_funcs do
    get_sum = fn x, y -> x + y end

    # whytf do I need a dot
    IO.puts("5 + 5 = #{get_sum.(5, 5)}")

    get_less = &(&1 - &2)
    IO.puts("7 - 3 = #{get_less.(7, 3)}")

    add_sum = fn
      {x, y} -> IO.puts("#{x} + #{y} = #{x + y}")
      {x, y, z} -> IO.puts("#{x} + #{y} + #{z} = #{x + y + z}")
    end

    add_sum.({1, 2})
    add_sum.({1, 2, 3})

    IO.puts(do_it())
  end

  # default values
  def do_it(x \\ 1, y \\ 1) do
    x + y
  end

  # recursion is used for looping as variables are immutable
  def factorial(num) do
    if num <= 1 do
      1
    else
      num * factorial(num - 1)
    end
  end

  def sum([]), do: 0

  def sum([head | tail]), do: head + sum(tail)

  def loop(max, min) do
    if max < min do
      nil
    else
      IO.puts("Number: #{max}")
      loop(max - 1, min)
    end
  end

  def enums do
    IO.puts(
      "Even list: #{Enum.all?([1, 2, 3],
      fn n -> rem(n, 2) == 0 end)}"
    )

    IO.puts(
      "Any even in list: #{Enum.any?([1, 2, 3],
      fn n -> rem(n, 2) == 0 end)}"
    )

    Enum.each([1, 2, 3], fn n -> IO.puts(n) end)

    double_list = Enum.map([1, 2, 3], fn n -> n * 2 end)

    summed = Enum.reduce(double_list, fn n, sum -> n + sum end)
    IO.puts("Summed: #{summed}")

    IO.inspect(Enum.uniq([1, 2, 2]))
  end

  def list_comprehensions do
    doubled = for n <- [1, 2, 3], do: n * 2
    IO.inspect(doubled)

    even_values = for n <- [1, 2, 3, 4], rem(n, 2) == 0, do: n
    IO.inspect(even_values)
  end

  def err_handling do
    err =
      try do
        5 / 0
      rescue
        ArithmeticError -> "Can't divide by zero"
      end

    IO.puts(err)
  end

  # goroutines for nubs
  def concurrency do
    spawn(fn -> loop(50, 1) end)
    spawn(fn -> loop(100, 50) end)

    send(self(), {:french, "Bob"})

    # if the atom was a string, we'd need a switch
    receive do
      {:german, name} -> IO.puts("Guten tag #{name}")
      {:french, name} -> IO.puts("Bonjour #{name}")
    after
      500 -> IO.puts("Time up")
    end
  end
end
