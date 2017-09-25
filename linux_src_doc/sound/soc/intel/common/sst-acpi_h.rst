.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/intel/common/sst-acpi.h

.. _`sst_codecs`:

struct sst_codecs
=================

.. c:type:: struct sst_codecs

    Structure to hold secondary codec information apart from the matched one, this data will be passed to the quirk function to match with the ACPI detected devices

.. _`sst_codecs.definition`:

Definition
----------

.. code-block:: c

    struct sst_codecs {
        int num_codecs;
        u8 codecs[SST_ACPI_MAX_CODECS][ACPI_ID_LEN];
    }

.. _`sst_codecs.members`:

Members
-------

num_codecs
    number of secondary codecs used in the platform

codecs
    holds the codec IDs

.. This file was automatic generated / don't edit.

