# FUMEplot
Facilitated visualisation of Uncertainty in Model Ensemble outputs using plots.

## local usage
For testing try:

```
python3 PlotEnsembleLines.py
```
(uses default, which is flee)

```
python3 PlotEnsembleLines.py flee
```

```
python3 PlotEnsembleLines.py homecoming
```

## usage with FabSim3 (fully automated)

FUMEplot acts as an independent plugin to FabSim3, enabling output plotting and analysis for a wide range of its supported codes. To install it, simply run:

```
fabsim localhost install_plugin:FUMEplot
```

Next, to use it, run *any* workflow, and fetch its results to the local machine using 

```
fabsim <machine> fetch_results
```

### Ensemble visualisation

At this point, FUMEplot can be invoked as follows for ensembles:

```
fabsim localhost fplot:<name_of_results_subdirectory>
```

FUMEplot will automatically detect the underlying solver, and construct the visualisations specified for that specific code.

### Replicated runs visualisation

Because replicated runs have a slightly different directory structure, FUMEplot should be used there as follows:

```
fabsim localhost fplot:<base_name_of_replica_run_subdirectory>
```

For example, if your replicas have names ranging from ```flee_archer2_24_replica_1``` to ```flee_archer2_24_replica_9```, then the ```base_name_of_replica_run_subdirectory``` should beset to ```flee_archer2_24_replica_```.


