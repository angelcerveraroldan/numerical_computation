import math


class Primes:
    primes_found = []

    def __init__(self, to):
        """
        Load all primes smaller than some upper bound to -- this will use the
        sieve of Eratosthenes which is O(to log(to))

        @param to: Natural number
        """

        # If the list is too small, then get next prime will not work,
        # since get next prime assumes that two primes differ by at least 2
        if to <= 3:
            self.primes_found = [2, 3, 5]
            return

        is_prime = [True if i % 2 == 1 else False for i in range(to + 1)]
        primes_found = [2]

        for i in range(3, to, 2):
            if not is_prime[i]:
                continue

            primes_found.append(i)

            num = i * i
            while num <= to:
                is_prime[num] = False
                num += i

        self.primes_found = primes_found

    def get_primes(self):
        return self.primes_found

    def _is_prime(self, i: int) -> bool:
        for prime in self.primes_found:
            if prime > math.sqrt(i):
                break

            if i % prime == 0:
                return False

        return True

    def find_next_n(self, n=1):
        maybe_prime = self.primes_found[-1] + 2
        found = 0

        while found < n:
            if self._is_prime(maybe_prime):
                self.primes_found.append(maybe_prime)
                found += 1

            maybe_prime += 2
