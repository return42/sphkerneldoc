
.. _module-parameters:

=================
Module Parameters
=================

There are standard module options for ALSA. At least, each module should have the ``index``, ``id`` and ``enable`` options.

If the module supports multiple cards (usually up to 8 = ``SNDRV_CARDS`` cards), they should be arrays. The default initial values are defined already as constants for easier
programming:


.. code-block:: c

      static int index[SNDRV_CARDS] = SNDRV_DEFAULT_IDX;
      static char &#x22C6;id[SNDRV_CARDS] = SNDRV_DEFAULT_STR;
      static int enable[SNDRV_CARDS] = SNDRV_DEFAULT_ENABLE_PNP;

If the module supports only a single card, they could be single variables, instead. ``enable`` option is not always necessary in this case, but it would be better to have a dummy
option for compatibility.

The module parameters must be declared with the standard ``module_param()()``, ``module_param_array()()`` and ``MODULE_PARM_DESC()`` macros.

The typical coding would be like below:


.. code-block:: c

      #define CARD_NAME "My Chip"

      module_param_array(index, int, NULL, 0444);
      MODULE_PARM_DESC(index, "Index value for " CARD_NAME " soundcard.");
      module_param_array(id, charp, NULL, 0444);
      MODULE_PARM_DESC(id, "ID string for " CARD_NAME " soundcard.");
      module_param_array(enable, bool, NULL, 0444);
      MODULE_PARM_DESC(enable, "Enable " CARD_NAME " soundcard.");

Also, don't forget to define the module description, classes, license and devices. Especially, the recent modprobe requires to define the module license as GPL, etc., otherwise the
system is shown as “tainted”.


.. code-block:: c

      MODULE_DESCRIPTION("My Chip");
      MODULE_LICENSE("GPL");
      MODULE_SUPPORTED_DEVICE("{{Vendor,My Chip Name}}");


