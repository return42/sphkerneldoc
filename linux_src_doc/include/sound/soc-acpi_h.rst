.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/sound/soc-acpi.h

.. _`snd_soc_acpi_codecs`:

struct snd_soc_acpi_codecs
==========================

.. c:type:: struct snd_soc_acpi_codecs

    Structure to hold secondary codec information apart from the matched one, this data will be passed to the quirk function to match with the ACPI detected devices

.. _`snd_soc_acpi_codecs.definition`:

Definition
----------

.. code-block:: c

    struct snd_soc_acpi_codecs {
        int num_codecs;
        u8 codecs[SND_SOC_ACPI_MAX_CODECS][ACPI_ID_LEN];
    }

.. _`snd_soc_acpi_codecs.members`:

Members
-------

num_codecs
    number of secondary codecs used in the platform

codecs
    holds the codec IDs

.. This file was automatic generated / don't edit.

