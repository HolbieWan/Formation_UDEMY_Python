from faker import Faker

fake = Faker(locale="fr_FR")

print(fake.name())
print(fake.address())
print(fake.text())
print(fake.name())

# for _ in range(50):
#  print(fake.unique.random_int())

numbers = [fake.unique.random_int() for _ in range(50)]

assert len(numbers) == len(set(numbers))  # leve assertionError if not unique

# !maximum de nom uniques: 1000

for _ in range(10):
  print(fake.job())
  print(fake.file_path(depth=5, category='video'))
  print(fake.credit_card_number(), fake.credit_card_expire(), fake.credit_card_security_code())
  print(fake.rgb_color())
  print(fake.hex_color())

  print(fake.numerify(text="%%%-%-%%%%-%%-##"))
  print(fake.bothify(text="Product Number: ???-#######"))