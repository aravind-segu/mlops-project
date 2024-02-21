import pathlib


def test_notebook_format():
    # Verify that all Databricks notebooks have the required header
    paths = list(pathlib.Path("./notebooks").glob("**/*.py"))
    for s in paths:
        notebook_str = open(str(s)).read()
        assert notebook_str.startswith("# Databricks notebook source")
