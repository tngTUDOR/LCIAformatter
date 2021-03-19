---
title: 'LCIA Formatter'
tags:
  - life cycle assessment
  - impact assessment
  - Python
authors:
  - name: Ben Young
    orcid: 0000-0001-6276-8670
    affiliation: 1
  - name: Michael Srocka
    orcid:
    affiliation: 2
  - name: Wesley Ingwersen^[Corresponding author]
    orcid: 0000-0002-9614-701X
    affiliation: 3
  - name: Ben Morelli
    orcid: 0000-0002-7660-6485
    affiliation: 1
  - name: Sarah Cashman
    orcid: 0000-0001-9859-9557
    affiliation: 1
  - name: Andrew Henderson
    orcid: 0000-0003-2436-7512
    affiliation: 1
affiliations:
 - name: Eastern Research Group, Inc. 
   index: 1
 - name: GreenDelta
   index: 2
 - name: U.S. Environmental Protection Agency
   index: 3
date: 15 March 2021
bibliography: paper.bib
---

# Summary

The United States Environmental Protection Agency (USEPA) is developing an automated life cycle assessment (LCA) tool ecosystem to comprehensively assess environmental and public health metrics across industries and products. The ecosystem includes tools to automate the creation of life cycle inventory (LCI) datasets, which account for flows to and from nature for steps across the life cycle of products or services, and life cycle impact assessment (LCIA) tools to support classification and characterization of the cumulative LCI to potential impacts [@international_organization_for_standardization_enivronmental_2006]. This paper describes a USEPA LCA ecosystem tool 'LCIA formatter' that extracts LCIA information from original source methods and converts the data for interoperability with the rest of the USEPA LCA ecosystem tools.   

# Statement of need

LCIA methods can be implemented in LCA software to provide impact assessment results for LCI data loaded into the software, but the flows (to and from nature) used in these LCIA methods must match exactly the flows (to and from nature) in the LCI data to ensure all relevant flows are captured in the LCA model results. As LCI flows are updated, the impact methods should also be made available, and vice versa, as LCIA method developers update characterization factors, they should be available as soon as possible to work with existing LCI data. The LCIA formatter module this paper describes is a specific solution to take LCIA methods from original providers, map them to an authoritative flow list, and export them in common data formats for use with LCI datasets mapped to the same authoritative flow list. The LCIA formatter is intended for integration with the Federal LCA Commons Elementary Flow List (FEDEFL), an authoritative nomenclature system of flows to and from nature for federal agencies in the U.S. to use when sharing data through the Federal LCA Commons [(FLCAC)](https://www.lcacommons.gov/) [@edelen_federal_2019].

# Structure

The LCIA formatter code is written in the Python 3.x language and primarily uses the latest pandas package for data storage and manipulation. The code is stored on a USEPA GitHub [repository](https://github.com/USEPA/LCIAformatter) and is available for public access.

The LCIA formatter accesses source methods directly from the data provider. These methods take the format of Excel files or Access databases. Source data are downloaded and saved in a temporary cache.
To support the specific functions necessary to access and parse individual methods, each method is processed within its own module. Flow names, indicators, characterization factors, and other metadata are compiled in a [standard format](https://github.com/USEPA/LCIAformatter/tree/documentation/format%20specs).
Adjustments are made as needed to improve consistency between indicators and across methods. This includes handling duplicate entries for the same elementary flow, data cleaning (such as cleaning string names, adjusting capitalization, formatting of CAS Registry Numbers).
Additionally, the LCIA formatter supports the inclusion of non specified secondary contexts (emission locations) where none are provided.
Where methods provide both midpoint and endpoint categories within a single source, the LCIA formatter parses these methods for separate use.
Finally, source flow data are mapped to elementary flows in the FEDEFL [@edelen_federal_2019], through mapping files provided within that [package](https://github.com/USEPA/Federal-LCA-Commons-Elementary-Flow-List). These mapping files correspond flow names and contexts to a common set of elementary flows generated for life cycle assessment modeling by the US EPA.
Mapped methods are stored locally as parquet files for future access by LCIA formatter or other tools.
Additionally, mapped methods can be exported as JSON-LD format for use in LCA software tools such as [openLCA](https://www.openlca.org/).


# Available Methods
The LCIA formatter is structured to easily convert original source data from existing LCIA methods. Version 1.0 of the LCIA formatter converts three commonly used LCIA methods: TRACI 2.1, ReCiPe2016, and ImpactWorld+. Available LCIA methods cover a variety of impact categories, with midpoint and/or endpoint indicators available at different points on the environmental cause-effect chain [@unep_glam_2016]. Cumulative LCI indicators based on the FEDEFL are also available as an output of the LCIA formatter.

## TRACI2.1
USEPA's Tool for Reduction and Assessment of Chemicals and Other Impacts (TRACI) is widely used for LCA across the U.S. Federal Government and by U.S.-based LCA practitioners [@bare_traci_2011]. The LCIA formatter accesses the TRACI Excel-based source file and characterizes impacts across 9 midpiont indicators for use in U.S.-focused analyses. When available, flow characterization factors are mapped to the release context with the greatest level of detail. For example, an air emission may be linked to the specific release height and population density of release. If such secondary context data is unknown, the LCIA formatter generates an average factor across the possible contexts to ensure the flow will still be captured in model calculations.

## ReCiPe2016 
ReCiPe 2016 characterizes impacts across 18 midpiont indicators and three perspectives: Individualist, Hierarchist, and Egalitarian [@huijbregts_recipe_2017]. The LCIA formatter generates endpoint impacts through a series of midpoint conversion factors provided for each indicator.
As is done for TRACI2.1, where characterization factors are not supplied for unspecified secondary contexts, an average factor across the possible contexts is generated. This ensures that users that do not specify a secondary context (e.g. emission to air with no indication of population density) can still obtain a characterization factor for a flow. 


## ImpactWorld+
ImpactWorld+ v1.3 is downloaded as an Access database and global flows are read into a pandas dataframe at midpoint and endpoint levels [@bulle_impact_2019]. Flows at native resolution or aggregated by landmass (continent, country, etc.) are currently excluded as they are not compatible with the FEDEFL at this time. Context information is added for water scarcity and availability categories, flowable name is applied as context for land occupation and transformation categories. Context descriptions are provided in the original source for all other categories.


## FEDEFL Inventory Methods
The LCIA formatter generates life cycle inventory methods based on groups of elementary flows identified in the FEDEFL. For example, an inventory method for energy resource use represents the summation of all instances of these flows within a dataset. Where necessary unit conversions are applied to achieve a consistent indicator unit. 

# Applications

The LCIA formatter also includes a method-agnostic approach to convert indicators (midpoint or endpoint) to monetary values.  The primary valuation is based on budget constraint modeling [@weidema_valuation_2009], updated to USD2014; conversions between the different ecosystem impact indicators (e.g., PDF.m2.yr and species.yr) are based on the species density calculations from ReCiPe 2008 [@goedkoop_recipe_2009].

The LCIA methods generated by the LCIA formatter for use with the FEDEFL are hosted publicly on the FLCAC for use by LCA practitioners and researchers. These methods support life cycle assessments performed by many parties, including member agencies for the Federal LCA Commons such as U.S. EPA, U.S. DOE, USDA, DOD, and others. These methods also enable impact assessment for researchers utilizing the US Life Cycle Inventory (USLCI) Database.
As a Python-based package, the LCIA formatter can also be accessed by the expanding ecosystem of publicly available tools for LCA automation, including [useeior](https://github.com/USEPA/useeior) and the Electricity Life Cycle Inventory ([electricitylci](https://github.com/USEPA/ElectricityLCI)).
The system was built to be flexible enough to support creating outputs for LCIA spatially-explicit characterization factors.



# Acknowledgements

The authors wish to acknolwedge additional support of the LCIA formatter from Ashley Edelen, Danny Hage, Troy Hottle, and Catherine Birney.

# References