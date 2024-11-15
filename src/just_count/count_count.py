import just_count.square
import click

@click.command()
@click.argument("square", type=int)

def main(square):
    print(f"The square of 5 is {just_count.square.square(square)}")

if __name__ == '__main__':
    main()