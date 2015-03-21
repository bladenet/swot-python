# Swot Python :apple:

This is a port of the popular Ruby Gem, "Swot" to Python.  As such, please do NOT make data
contributions to this repository. Contribute any new academic domain names to the Ruby version
of this package at https://github.com/leereilly/swot. Please follow the
[contribution guidelines](https://github.com/leereilly/swot/blob/master/CONTRIBUTING.md) noted in
the Ruby Swot repository.

I will be pulling changes to upstream domain data.

> If you have a product or service and offer **academic discounts**, there's a good chance there's some manual
> component to the approval process. Perhaps `.edu` email addresses are automatically approved because, for the most
> part at least, they're associated with American post-secondary educational institutions. Perhaps `.ac.uk` email
> addresses are automatically approved because they're guaranteed to belong to British universities and colleges.
> Unfortunately, not every country has an education-specific TLD (Top Level Domain) and plenty of schools use `.com`
> or `.net`.

> Swot is a community-driven or crowdsourced library for verifying that domain names and email addresses are tied to
> a legitimate university of college - more specifically, an academic institution providing higher education in
> tertiary, quaternary or any other kind of post-secondary education in any country in the world.

### Installation

```
python setup.py install
```

### Usage

**Native**

```python
from swot import Swot
Swot.is_academic('utoronto.ca')
Swot.is_academic('lreilly@stanford.edu')
Swot.is_academic('http://utoronto.ca')
```
