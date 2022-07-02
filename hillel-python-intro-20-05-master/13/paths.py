import os.path
import pathlib


plan_12_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "12",
    "plan.md"
)
print(plan_12_path)

with open(plan_12_path, mode="r") as plan:
    print(plan.read())


plan_12_path = pathlib.Path(__file__).parent.parent / "12" / "plan.md"
print(plan_12_path.read_text())

print(__file__)

# Difference
# os.path - works with paths as strings
# pathlib - works with paths as objects (classes)
