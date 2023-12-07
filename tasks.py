"""
This is a plugin example. This will be placed in {taskfiles_location}/_plugins/{name}
"""
from invoke import task, Context


@task()
def say_hello(ctx: Context):
    ctx.run("echo 'Hello world'")