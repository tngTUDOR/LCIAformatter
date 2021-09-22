# LCIA formatter

The LCIA formatter, or `lciafmt`, is a Python tool for standardizing the format and flows of life cycle impact assessment (LCIA) data. The tool acquires LCIA data transparently from its original 
source, cleans the data, shapes them into a standard format using the [LCIAmethod format](./format%20specs/LCIAmethod.md), and optionally applies flow mappings as defined in the [Federal LCA Commons Elementary Flow List](https://github.com/USEPA/Federal-LCA-Commons-Elementary-Flow-List). The result can be exported to all formats supported by the
`pandas` package (e.g. Excel, CSV) or the [openLCA JSON-LD format](https://github.com/GreenDelta/olca-schema).

## Data Provided

	|LCIA Data | Provider | Link |
	|--------- | -------- | ---- |
	|TRACI 2.1 | US Environmental Protection Agency | [Tool for Reduction and Assessment of Chemicals and Other Environmental Impacts](https://www.epa.gov/chemical-research/tool-reduction-and-assessment-chemicals-and-other-environmental-impacts-traci)|
	|ReCiPe 2016 Midpoint | National Institute for Public Health and the Environment (The Netherlands) | [LCIA: the ReCiPe Model](https://www.rivm.nl/en/life-cycle-assessment-lca/recipe)|
	|ReCiPe 2016 Endpoint | National Institute for Public Health and the Environment (The Netherlands) | [LCIA: the ReCiPe Model](https://www.rivm.nl/en/life-cycle-assessment-lca/recipe)|
	|ImpactWorld+ Midpoint¹| International Reference Center for Life Cycle of Products, Services and Systems (CIRAIG) | [ImpactWorld+](http://www.impactworldplus.org/en/team.php)|
	|ImpactWorld+ Endpoint¹ | International Reference Center for Life Cycle of Products, Services and Systems (CIRAIG) | [ImpactWorld+](http://www.impactworldplus.org/en/team.php)|
	|FEDEFL Inventory Methods | US Environmental Protection Agency | [FEDEFL Inventory Methods](https://github.com/USEPA/LCIAformatter/wiki/Inventory-Methods)|

¹ only works on Windows installations

## Installation Instructions

Install a release directly from github using pip. From a command line interface, run:

> pip install git+https://github.com/USEPA/LCIAformatter.git@v1.0.0#egg=lciafmt

where you can replace 'v1.0.0' with the version you wish to use under [Releases](https://github.com/USEPA/LCIAformatter/releases).

Alternatively, to install from the most current point on the repository:

```
git clone https://github.com/USEPA/LCIAformatter.git
cd LCIAformatter
pip install . # or pip install -e . for devs
```

The current version contains an optional dependency on the `pyodbc` library to generate the Impact World+ LCIA method.
Due to limitations in reading Access databases from non-Windows platforms, this will only be install on Windows machines.
 
This needs to be specified in the pip install command. It can be done in one of two ways:

```
pip install .["ImpactWorld"]
```

or

```
pip install . -r requirements.txt -r impactworld_requirements.txt 
```

See the [Wiki](https://github.com/USEPA/LCIAformatter/wiki/) for further installation and [use instructions](https://github.com/USEPA/LCIAformatter/wiki/Using-lciafmt) or for information on how to seek [support](https://github.com/USEPA/LCIAformatter/wiki/Support).

## Disclaimer

The United States Environmental Protection Agency (EPA) GitHub project code is provided on an "as is" basis
and the user assumes responsibility for its use.  EPA has relinquished control of the information and no longer
has responsibility to protect the integrity , confidentiality, or availability of the information.  Any
reference to specific commercial products, processes, or services by service mark, trademark, manufacturer,
or otherwise, does not constitute or imply their endorsement, recommendation or favoring by EPA.  The EPA seal
and logo shall not be used in any manner to imply endorsement of any commercial product or activity by EPA or
the United States Government.
