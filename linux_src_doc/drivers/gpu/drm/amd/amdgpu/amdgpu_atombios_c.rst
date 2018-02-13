.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_atombios.c

.. _`cail_pll_read`:

cail_pll_read
=============

.. c:function:: uint32_t cail_pll_read(struct card_info *info, uint32_t reg)

    read PLL register

    :param struct card_info \*info:
        atom card_info pointer

    :param uint32_t reg:
        PLL register offset

.. _`cail_pll_read.description`:

Description
-----------

Provides a PLL register accessor for the atom interpreter (r4xx+).
Returns the value of the PLL register.

.. _`cail_pll_write`:

cail_pll_write
==============

.. c:function:: void cail_pll_write(struct card_info *info, uint32_t reg, uint32_t val)

    write PLL register

    :param struct card_info \*info:
        atom card_info pointer

    :param uint32_t reg:
        PLL register offset

    :param uint32_t val:
        value to write to the pll register

.. _`cail_pll_write.description`:

Description
-----------

Provides a PLL register accessor for the atom interpreter (r4xx+).

.. _`cail_mc_read`:

cail_mc_read
============

.. c:function:: uint32_t cail_mc_read(struct card_info *info, uint32_t reg)

    read MC (Memory Controller) register

    :param struct card_info \*info:
        atom card_info pointer

    :param uint32_t reg:
        MC register offset

.. _`cail_mc_read.description`:

Description
-----------

Provides an MC register accessor for the atom interpreter (r4xx+).
Returns the value of the MC register.

.. _`cail_mc_write`:

cail_mc_write
=============

.. c:function:: void cail_mc_write(struct card_info *info, uint32_t reg, uint32_t val)

    write MC (Memory Controller) register

    :param struct card_info \*info:
        atom card_info pointer

    :param uint32_t reg:
        MC register offset

    :param uint32_t val:
        value to write to the pll register

.. _`cail_mc_write.description`:

Description
-----------

Provides a MC register accessor for the atom interpreter (r4xx+).

.. _`cail_reg_write`:

cail_reg_write
==============

.. c:function:: void cail_reg_write(struct card_info *info, uint32_t reg, uint32_t val)

    write MMIO register

    :param struct card_info \*info:
        atom card_info pointer

    :param uint32_t reg:
        MMIO register offset

    :param uint32_t val:
        value to write to the pll register

.. _`cail_reg_write.description`:

Description
-----------

Provides a MMIO register accessor for the atom interpreter (r4xx+).

.. _`cail_reg_read`:

cail_reg_read
=============

.. c:function:: uint32_t cail_reg_read(struct card_info *info, uint32_t reg)

    read MMIO register

    :param struct card_info \*info:
        atom card_info pointer

    :param uint32_t reg:
        MMIO register offset

.. _`cail_reg_read.description`:

Description
-----------

Provides an MMIO register accessor for the atom interpreter (r4xx+).
Returns the value of the MMIO register.

.. _`cail_ioreg_write`:

cail_ioreg_write
================

.. c:function:: void cail_ioreg_write(struct card_info *info, uint32_t reg, uint32_t val)

    write IO register

    :param struct card_info \*info:
        atom card_info pointer

    :param uint32_t reg:
        IO register offset

    :param uint32_t val:
        value to write to the pll register

.. _`cail_ioreg_write.description`:

Description
-----------

Provides a IO register accessor for the atom interpreter (r4xx+).

.. _`cail_ioreg_read`:

cail_ioreg_read
===============

.. c:function:: uint32_t cail_ioreg_read(struct card_info *info, uint32_t reg)

    read IO register

    :param struct card_info \*info:
        atom card_info pointer

    :param uint32_t reg:
        IO register offset

.. _`cail_ioreg_read.description`:

Description
-----------

Provides an IO register accessor for the atom interpreter (r4xx+).
Returns the value of the IO register.

.. _`amdgpu_atombios_fini`:

amdgpu_atombios_fini
====================

.. c:function:: void amdgpu_atombios_fini(struct amdgpu_device *adev)

    free the driver info and callbacks for atombios

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_atombios_fini.description`:

Description
-----------

Frees the driver info and register access callbacks for the ATOM
interpreter (r4xx+).
Called at driver shutdown.

.. _`amdgpu_atombios_init`:

amdgpu_atombios_init
====================

.. c:function:: int amdgpu_atombios_init(struct amdgpu_device *adev)

    init the driver info and callbacks for atombios

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_atombios_init.description`:

Description
-----------

Initializes the driver info and register access callbacks for the
ATOM interpreter (r4xx+).
Returns 0 on sucess, -ENOMEM on failure.
Called at driver startup.

.. This file was automatic generated / don't edit.

