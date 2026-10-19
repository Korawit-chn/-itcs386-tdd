# Reflection
6688013 Korawit Chantavilaiying

1. I wrote 10 tests and 40 lines of production code. The ratio is 1:4.

2. Step A6 (simple addition). I had to understand a lot of new behaviour at once: `plus`, the new `Sum` class, and the `Converter` with `reduce`. It took time to understand why `plus` returns a `Sum` instead of a `Quantity`, and how the work is passed from `Converter.reduce` to `Sum.reduce`.

3. Fake It: `plus` returned `grams(500)`. The choice was right, but I forgot to remove the fake and the tests still passed, because one example can't catch a fake.
   Triangulation: I tested `200 g × 3` and then `200 g × 2`, so `times` had to really multiply. The choice was right.
   Obvious Implementation: `Sum.times` and `Converter.rate`. They were simple enough to write directly, so the choice was right.

4. All items on the list are done. Next I would implement deletion

5. No. On paper because I think it too complicate

6. In Part 0, writing tests after the code felt like checking for bugs in finished work. In Part A, I feel it more harder because I don't actually know the whole program and have to make it from test make it harder when adding new feature.