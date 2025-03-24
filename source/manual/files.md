# Files

## Naming

The naming convention of the downloaded files consists of five parts:
the *region*, *realization*, *location*, *direction* and *quantity*.

```{eval-rst}
.. figure:: figures/naming.svg
   :align: center
   :width: 50%

   Naming convention of downloaded files.
```

### Region

See {ref}`region`.

### Location

The location is identified by three integers, separated by two underscores (``_``). These
integers identify the index of the point in the grid. In order these correspond to:

1. The coordinate parallel to the fault,
2. The coordinate normal to the fault, and
3. The vertical coordinate.

### Direction

The direction mark is one of the following two-letter identifiers:

```{csv-table}
    ``FP``, Fault Parallel
    ``FN``, Fault Normal
    ``UP``, Vertical
```

### Quantity

The *quantity* is one of:

```{eval-rst}
.. csv-table::

    ``AT2``, Acceleration
    ``VT2``, Velocity
    ``DT2``, Displacement
```