import click
from .naoc import citation_stats
from .config import save_token, load_token, token_exists, get_token_path


@click.group()
def cli():
    """hypergravity command line interface"""
    pass


@cli.group()
def token():
    """Manage ADSABS token"""
    pass


@token.command(name="set")
@click.argument("token_value")
def set_token(token_value):
    """Set ADSABS token and save to ~/.hypergravity/ads_token"""
    token_path = save_token(token_value)
    click.echo(f"\033[1;32m✅ Token saved successfully to: {token_path}\033[0m")
    click.echo(f"   Token preview: {token_value[:10]}...{token_value[-5:]}")


@token.command(name="show")
def show_token():
    """Show current ADSABS token"""
    if not token_exists():
        click.echo("\033[1;33m⚠️  No token found! Please set token first using: citation token set xxx\033[0m")
        return
    
    token = load_token()
    token_path = get_token_path()
    click.echo(f"\033[1;36m📄 Current token from: {token_path}\033[0m")
    click.echo(f"   Token: {token}")


@cli.command(name="stats")
@click.option("--bibcode", default="2020ApJS..246....9Z", help="Bibcode of the article")
@click.option("--year", default="2000-2022", help="Year range for citations, e.g., 2020-2025")
@click.option("--token", default=None, help="ADSABS token (optional, uses saved token if not provided)")
@click.option("--verbose", is_flag=True, default=True, help="Print verbose information")
def stats(bibcode, year, token, verbose):
    """Count refereed citation by others"""
    result = citation_stats(bibcode=bibcode, year=year, token=token, verbose=verbose)
    click.echo("\n" + "=" * 80)
    click.echo("他引统计结果请查看网页：")
    click.echo("=" * 80)
    result.pprint(max_lines=-1, max_width=-1)


if __name__ == "__main__":
    cli()
