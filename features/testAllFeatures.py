if __name__ == '__main__':
    from behave import __main__ as behave_executable
    behave_executable.main(args="--tags= @test1 features/")


