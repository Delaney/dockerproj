#!/usr/bin/env python
import click

@click.command()
def hello():
    click.echo("Hello Wurld!")
    
if __name__ == '__main__':
    hello()