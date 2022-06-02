import click
import mlrun

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', default="aaaaa", help='Number of greetings.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")
        
    context = mlrun.get_or_create_ctx("train")
    context.logger.info("mlrun logging")
    context.log_result("accuracy", 0.93)

if __name__ == '__main__':
    hello()