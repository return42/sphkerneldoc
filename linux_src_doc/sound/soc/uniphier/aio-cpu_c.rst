.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/uniphier/aio-cpu.c

.. _`find_volume`:

find_volume
===========

.. c:function:: struct uniphier_aio_sub *find_volume(struct uniphier_aio_chip *chip, int oport_hw)

    find volume supported HW port by HW port number

    :param struct uniphier_aio_chip \*chip:
        the AIO chip pointer

    :param int oport_hw:
        HW port number, one of AUD_HW_XXXX

.. _`find_volume.description`:

Description
-----------

Find AIO device from device list by HW port number. Volume feature is
available only in Output and PCM ports, this limitation comes from HW
specifications.

.. _`find_volume.return`:

Return
------

The pointer of AIO substream if successful, otherwise NULL on error.

.. _`find_spec`:

find_spec
=========

.. c:function:: const struct uniphier_aio_spec *find_spec(struct uniphier_aio *aio, const char *name, int direction)

    find HW specification info by name

    :param struct uniphier_aio \*aio:
        the AIO device pointer

    :param const char \*name:
        name of device

    :param int direction:
        the direction of substream, SNDRV_PCM_STREAM\_\*

.. _`find_spec.description`:

Description
-----------

Find hardware specification information from list by device name. This
information is used for telling the difference of SoCs to driver.

Specification list is array of 'struct uniphier_aio_spec' which is defined
in each drivers (see: aio-i2s.c).

.. _`find_spec.return`:

Return
------

The pointer of hardware specification of AIO if successful,
otherwise NULL on error.

.. _`find_divider`:

find_divider
============

.. c:function:: int find_divider(struct uniphier_aio *aio, int pll_id, unsigned int freq)

    find clock divider by frequency

    :param struct uniphier_aio \*aio:
        the AIO device pointer

    :param int pll_id:
        PLL ID, should be AUD_PLL_XX

    :param unsigned int freq:
        required frequency

.. _`find_divider.description`:

Description
-----------

Find suitable clock divider by frequency.

.. _`find_divider.return`:

Return
------

The ID of PLL if successful, otherwise negative error value.

.. This file was automatic generated / don't edit.

