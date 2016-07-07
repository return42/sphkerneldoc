.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/edac/ppc4xx_edac.c

.. _`mfsdram`:

mfsdram
=======

.. c:function:: u32 mfsdram(const dcr_host_t *dcr_host, unsigned int idcr_n)

    read and return controller register data

    :param const dcr_host_t \*dcr_host:
        A pointer to the DCR mapping.

    :param unsigned int idcr_n:
        The indirect DCR register to read.

.. _`mfsdram.description`:

Description
-----------

This routine reads and returns the data associated with the
controller's specified indirect DCR register.

Returns the read data.

.. _`mtsdram`:

mtsdram
=======

.. c:function:: void mtsdram(const dcr_host_t *dcr_host, unsigned int idcr_n, u32 value)

    write controller register data

    :param const dcr_host_t \*dcr_host:
        A pointer to the DCR mapping.

    :param unsigned int idcr_n:
        The indirect DCR register to write.

    :param u32 value:
        The data to write.

.. _`mtsdram.description`:

Description
-----------

This routine writes the provided data to the controller's specified
indirect DCR register.

.. _`ppc4xx_edac_check_bank_error`:

ppc4xx_edac_check_bank_error
============================

.. c:function:: bool ppc4xx_edac_check_bank_error(const struct ppc4xx_ecc_status *status, unsigned int bank)

    check a bank for an ECC bank error

    :param const struct ppc4xx_ecc_status \*status:
        A pointer to the ECC status structure to check for an
        ECC bank error.

    :param unsigned int bank:
        The bank to check for an ECC error.

.. _`ppc4xx_edac_check_bank_error.description`:

Description
-----------

This routine determines whether the specified bank has an ECC
error.

Returns true if the specified bank has an ECC error; otherwise,
false.

.. _`ppc4xx_edac_generate_bank_message`:

ppc4xx_edac_generate_bank_message
=================================

.. c:function:: int ppc4xx_edac_generate_bank_message(const struct mem_ctl_info *mci, const struct ppc4xx_ecc_status *status, char *buffer, size_t size)

    generate interpretted bank status message

    :param const struct mem_ctl_info \*mci:
        A pointer to the EDAC memory controller instance associated
        with the bank message being generated.

    :param const struct ppc4xx_ecc_status \*status:
        A pointer to the ECC status structure to generate the
        message from.

    :param char \*buffer:
        A pointer to the buffer in which to generate the
        message.

    :param size_t size:
        The size, in bytes, of space available in buffer.

.. _`ppc4xx_edac_generate_bank_message.description`:

Description
-----------

This routine generates to the provided buffer the portion of the
driver-unique report message associated with the ECCESS[BKNER]
field of the specified ECC status.

Returns the number of characters generated on success; otherwise, <
0 on error.

.. _`ppc4xx_edac_generate_checkbit_message`:

ppc4xx_edac_generate_checkbit_message
=====================================

.. c:function:: int ppc4xx_edac_generate_checkbit_message(const struct mem_ctl_info *mci, const struct ppc4xx_ecc_status *status, char *buffer, size_t size)

    generate interpretted checkbit message

    :param const struct mem_ctl_info \*mci:
        A pointer to the EDAC memory controller instance associated
        with the checkbit message being generated.

    :param const struct ppc4xx_ecc_status \*status:
        A pointer to the ECC status structure to generate the
        message from.

    :param char \*buffer:
        A pointer to the buffer in which to generate the
        message.

    :param size_t size:
        The size, in bytes, of space available in buffer.

.. _`ppc4xx_edac_generate_checkbit_message.description`:

Description
-----------

This routine generates to the provided buffer the portion of the
driver-unique report message associated with the ECCESS[CKBER]
field of the specified ECC status.

Returns the number of characters generated on success; otherwise, <
0 on error.

.. _`ppc4xx_edac_generate_lane_message`:

ppc4xx_edac_generate_lane_message
=================================

.. c:function:: int ppc4xx_edac_generate_lane_message(const struct mem_ctl_info *mci, const struct ppc4xx_ecc_status *status, char *buffer, size_t size)

    generate interpretted byte lane message

    :param const struct mem_ctl_info \*mci:
        A pointer to the EDAC memory controller instance associated
        with the byte lane message being generated.

    :param const struct ppc4xx_ecc_status \*status:
        A pointer to the ECC status structure to generate the
        message from.

    :param char \*buffer:
        A pointer to the buffer in which to generate the
        message.

    :param size_t size:
        The size, in bytes, of space available in buffer.

.. _`ppc4xx_edac_generate_lane_message.description`:

Description
-----------

This routine generates to the provided buffer the portion of the
driver-unique report message associated with the ECCESS[BNCE]
field of the specified ECC status.

Returns the number of characters generated on success; otherwise, <
0 on error.

.. _`ppc4xx_edac_generate_ecc_message`:

ppc4xx_edac_generate_ecc_message
================================

.. c:function:: int ppc4xx_edac_generate_ecc_message(const struct mem_ctl_info *mci, const struct ppc4xx_ecc_status *status, char *buffer, size_t size)

    generate interpretted ECC status message

    :param const struct mem_ctl_info \*mci:
        A pointer to the EDAC memory controller instance associated
        with the ECCES message being generated.

    :param const struct ppc4xx_ecc_status \*status:
        A pointer to the ECC status structure to generate the
        message from.

    :param char \*buffer:
        A pointer to the buffer in which to generate the
        message.

    :param size_t size:
        The size, in bytes, of space available in buffer.

.. _`ppc4xx_edac_generate_ecc_message.description`:

Description
-----------

This routine generates to the provided buffer the portion of the
driver-unique report message associated with the ECCESS register of
the specified ECC status.

Returns the number of characters generated on success; otherwise, <
0 on error.

.. _`ppc4xx_edac_generate_plb_message`:

ppc4xx_edac_generate_plb_message
================================

.. c:function:: int ppc4xx_edac_generate_plb_message(const struct mem_ctl_info *mci, const struct ppc4xx_ecc_status *status, char *buffer, size_t size)

    generate interpretted PLB status message

    :param const struct mem_ctl_info \*mci:
        A pointer to the EDAC memory controller instance associated
        with the PLB message being generated.

    :param const struct ppc4xx_ecc_status \*status:
        A pointer to the ECC status structure to generate the
        message from.

    :param char \*buffer:
        A pointer to the buffer in which to generate the
        message.

    :param size_t size:
        The size, in bytes, of space available in buffer.

.. _`ppc4xx_edac_generate_plb_message.description`:

Description
-----------

This routine generates to the provided buffer the portion of the
driver-unique report message associated with the PLB-related BESR
and/or WMIRQ registers of the specified ECC status.

Returns the number of characters generated on success; otherwise, <
0 on error.

.. _`ppc4xx_edac_generate_message`:

ppc4xx_edac_generate_message
============================

.. c:function:: void ppc4xx_edac_generate_message(const struct mem_ctl_info *mci, const struct ppc4xx_ecc_status *status, char *buffer, size_t size)

    generate interpretted status message

    :param const struct mem_ctl_info \*mci:
        A pointer to the EDAC memory controller instance associated
        with the driver-unique message being generated.

    :param const struct ppc4xx_ecc_status \*status:
        A pointer to the ECC status structure to generate the
        message from.

    :param char \*buffer:
        A pointer to the buffer in which to generate the
        message.

    :param size_t size:
        The size, in bytes, of space available in buffer.

.. _`ppc4xx_edac_generate_message.description`:

Description
-----------

This routine generates to the provided buffer the driver-unique
EDAC report message from the specified ECC status.

.. _`ppc4xx_ecc_dump_status`:

ppc4xx_ecc_dump_status
======================

.. c:function:: void ppc4xx_ecc_dump_status(const struct mem_ctl_info *mci, const struct ppc4xx_ecc_status *status)

    dump controller ECC status registers

    :param const struct mem_ctl_info \*mci:
        A pointer to the EDAC memory controller instance
        associated with the status being dumped.

    :param const struct ppc4xx_ecc_status \*status:
        A pointer to the ECC status structure to generate the
        dump from.

.. _`ppc4xx_ecc_dump_status.description`:

Description
-----------

This routine dumps to the kernel log buffer the raw and
interpretted specified ECC status.

.. _`ppc4xx_ecc_get_status`:

ppc4xx_ecc_get_status
=====================

.. c:function:: void ppc4xx_ecc_get_status(const struct mem_ctl_info *mci, struct ppc4xx_ecc_status *status)

    get controller ECC status

    :param const struct mem_ctl_info \*mci:
        A pointer to the EDAC memory controller instance
        associated with the status being retrieved.

    :param struct ppc4xx_ecc_status \*status:
        A pointer to the ECC status structure to populate the
        ECC status with.

.. _`ppc4xx_ecc_get_status.description`:

Description
-----------

This routine reads and masks, as appropriate, all the relevant
status registers that deal with ibm,sdram-4xx-ddr2 ECC errors.
While we read all of them, for correctable errors, we only expect
to deal with ECCES. For uncorrectable errors, we expect to deal
with all of them.

.. _`ppc4xx_ecc_clear_status`:

ppc4xx_ecc_clear_status
=======================

.. c:function:: void ppc4xx_ecc_clear_status(const struct mem_ctl_info *mci, const struct ppc4xx_ecc_status *status)

    clear controller ECC status

    :param const struct mem_ctl_info \*mci:
        A pointer to the EDAC memory controller instance
        associated with the status being cleared.

    :param const struct ppc4xx_ecc_status \*status:
        A pointer to the ECC status structure containing the
        values to write to clear the ECC status.

.. _`ppc4xx_ecc_clear_status.description`:

Description
-----------

This routine clears--by writing the masked (as appropriate) status
values back to--the status registers that deal with
ibm,sdram-4xx-ddr2 ECC errors.

.. _`ppc4xx_edac_handle_ce`:

ppc4xx_edac_handle_ce
=====================

.. c:function:: void ppc4xx_edac_handle_ce(struct mem_ctl_info *mci, const struct ppc4xx_ecc_status *status)

    handle controller correctable ECC error (CE)

    :param struct mem_ctl_info \*mci:
        A pointer to the EDAC memory controller instance
        associated with the correctable error being handled and reported.

    :param const struct ppc4xx_ecc_status \*status:
        A pointer to the ECC status structure associated with
        the correctable error being handled and reported.

.. _`ppc4xx_edac_handle_ce.description`:

Description
-----------

This routine handles an ibm,sdram-4xx-ddr2 controller ECC
correctable error. Per the aforementioned discussion, there's not
enough status available to use the full EDAC correctable error
interface, so we just pass driver-unique message to the "no info"
interface.

.. _`ppc4xx_edac_handle_ue`:

ppc4xx_edac_handle_ue
=====================

.. c:function:: void ppc4xx_edac_handle_ue(struct mem_ctl_info *mci, const struct ppc4xx_ecc_status *status)

    handle controller uncorrectable ECC error (UE)

    :param struct mem_ctl_info \*mci:
        A pointer to the EDAC memory controller instance
        associated with the uncorrectable error being handled and
        reported.

    :param const struct ppc4xx_ecc_status \*status:
        A pointer to the ECC status structure associated with
        the uncorrectable error being handled and reported.

.. _`ppc4xx_edac_handle_ue.description`:

Description
-----------

This routine handles an ibm,sdram-4xx-ddr2 controller ECC
uncorrectable error.

.. _`ppc4xx_edac_check`:

ppc4xx_edac_check
=================

.. c:function:: void ppc4xx_edac_check(struct mem_ctl_info *mci)

    check controller for ECC errors

    :param struct mem_ctl_info \*mci:
        A pointer to the EDAC memory controller instance
        associated with the ibm,sdram-4xx-ddr2 controller being
        checked.

.. _`ppc4xx_edac_check.description`:

Description
-----------

This routine is used to check and post ECC errors and is called by
both the EDAC polling thread and this driver's CE and UE interrupt
handler.

.. _`ppc4xx_edac_isr`:

ppc4xx_edac_isr
===============

.. c:function:: irqreturn_t ppc4xx_edac_isr(int irq, void *dev_id)

    SEC (CE) and DED (UE) interrupt service routine

    :param int irq:
        The virtual interrupt number being serviced.

    :param void \*dev_id:
        A pointer to the EDAC memory controller instance
        associated with the interrupt being handled.

.. _`ppc4xx_edac_isr.description`:

Description
-----------

This routine implements the interrupt handler for both correctable
(CE) and uncorrectable (UE) ECC errors for the ibm,sdram-4xx-ddr2
controller. It simply calls through to the same routine used during
polling to check, report and clear the ECC status.

Unconditionally returns IRQ_HANDLED.

.. _`ppc4xx_edac_get_dtype`:

ppc4xx_edac_get_dtype
=====================

.. c:function:: enum dev_type ppc4xx_edac_get_dtype(u32 mcopt1)

    return the controller memory width

    :param u32 mcopt1:
        The 32-bit Memory Controller Option 1 register value
        currently set for the controller, from which the width
        is derived.

.. _`ppc4xx_edac_get_dtype.description`:

Description
-----------

This routine returns the EDAC device type width appropriate for the
current controller configuration.

.. _`ppc4xx_edac_get_dtype.todo`:

TODO
----

This needs to be conditioned dynamically through feature
flags or some such when other controller variants are supported as
the 405EX[r] is 16-/32-bit and the others are 32-/64-bit with the
16- and 64-bit field definition/value/enumeration (b1) overloaded
among them.

Returns a device type width enumeration.

.. _`ppc4xx_edac_get_mtype`:

ppc4xx_edac_get_mtype
=====================

.. c:function:: enum mem_type ppc4xx_edac_get_mtype(u32 mcopt1)

    return controller memory type

    :param u32 mcopt1:
        The 32-bit Memory Controller Option 1 register value
        currently set for the controller, from which the memory type
        is derived.

.. _`ppc4xx_edac_get_mtype.description`:

Description
-----------

This routine returns the EDAC memory type appropriate for the
current controller configuration.

Returns a memory type enumeration.

.. _`ppc4xx_edac_init_csrows`:

ppc4xx_edac_init_csrows
=======================

.. c:function:: int ppc4xx_edac_init_csrows(struct mem_ctl_info *mci, u32 mcopt1)

    initialize driver instance rows

    :param struct mem_ctl_info \*mci:
        A pointer to the EDAC memory controller instance
        associated with the ibm,sdram-4xx-ddr2 controller for which
        the csrows (i.e. banks/ranks) are being initialized.

    :param u32 mcopt1:
        The 32-bit Memory Controller Option 1 register value
        currently set for the controller, from which bank width
        and memory typ information is derived.

.. _`ppc4xx_edac_init_csrows.description`:

Description
-----------

This routine initializes the virtual "chip select rows" associated
with the EDAC memory controller instance. An ibm,sdram-4xx-ddr2
controller bank/rank is mapped to a row.

Returns 0 if OK; otherwise, -EINVAL if the memory bank size
configuration cannot be determined.

.. _`ppc4xx_edac_mc_init`:

ppc4xx_edac_mc_init
===================

.. c:function:: int ppc4xx_edac_mc_init(struct mem_ctl_info *mci, struct platform_device *op, const dcr_host_t *dcr_host, u32 mcopt1)

    initialize driver instance

    :param struct mem_ctl_info \*mci:
        A pointer to the EDAC memory controller instance being
        initialized.

    :param struct platform_device \*op:
        A pointer to the OpenFirmware device tree node associated
        with the controller this EDAC instance is bound to.

    :param const dcr_host_t \*dcr_host:
        A pointer to the DCR data containing the DCR mapping
        for this controller instance.

    :param u32 mcopt1:
        The 32-bit Memory Controller Option 1 register value
        currently set for the controller, from which ECC capabilities
        and scrub mode are derived.

.. _`ppc4xx_edac_mc_init.description`:

Description
-----------

This routine performs initialization of the EDAC memory controller
instance and related driver-private data associated with the
ibm,sdram-4xx-ddr2 memory controller the instance is bound to.

Returns 0 if OK; otherwise, < 0 on error.

.. _`ppc4xx_edac_register_irq`:

ppc4xx_edac_register_irq
========================

.. c:function:: int ppc4xx_edac_register_irq(struct platform_device *op, struct mem_ctl_info *mci)

    setup and register controller interrupts

    :param struct platform_device \*op:
        A pointer to the OpenFirmware device tree node associated
        with the controller this EDAC instance is bound to.

    :param struct mem_ctl_info \*mci:
        A pointer to the EDAC memory controller instance
        associated with the ibm,sdram-4xx-ddr2 controller for which
        interrupts are being registered.

.. _`ppc4xx_edac_register_irq.description`:

Description
-----------

This routine parses the correctable (CE) and uncorrectable error (UE)
interrupts from the device tree node and maps and assigns them to
the associated EDAC memory controller instance.

Returns 0 if OK; otherwise, -ENODEV if the interrupts could not be
mapped and assigned.

.. _`ppc4xx_edac_map_dcrs`:

ppc4xx_edac_map_dcrs
====================

.. c:function:: int ppc4xx_edac_map_dcrs(const struct device_node *np, dcr_host_t *dcr_host)

    locate and map controller registers

    :param const struct device_node \*np:
        A pointer to the device tree node containing the DCR
        resources to map.

    :param dcr_host_t \*dcr_host:
        A pointer to the DCR data to populate with the
        DCR mapping.

.. _`ppc4xx_edac_map_dcrs.description`:

Description
-----------

This routine attempts to locate in the device tree and map the DCR
register resources associated with the controller's indirect DCR
address and data windows.

Returns 0 if the DCRs were successfully mapped; otherwise, < 0 on
error.

.. _`ppc4xx_edac_probe`:

ppc4xx_edac_probe
=================

.. c:function:: int ppc4xx_edac_probe(struct platform_device *op)

    check controller and bind driver

    :param struct platform_device \*op:
        A pointer to the OpenFirmware device tree node associated
        with the controller being probed for driver binding.

.. _`ppc4xx_edac_probe.description`:

Description
-----------

This routine probes a specific ibm,sdram-4xx-ddr2 controller
instance for binding with the driver.

Returns 0 if the controller instance was successfully bound to the
driver; otherwise, < 0 on error.

.. _`ppc4xx_edac_remove`:

ppc4xx_edac_remove
==================

.. c:function:: int ppc4xx_edac_remove(struct platform_device *op)

    unbind driver from controller

    :param struct platform_device \*op:
        A pointer to the OpenFirmware device tree node associated
        with the controller this EDAC instance is to be unbound/removed
        from.

.. _`ppc4xx_edac_remove.description`:

Description
-----------

This routine unbinds the EDAC memory controller instance associated
with the specified ibm,sdram-4xx-ddr2 controller described by the
OpenFirmware device tree node passed as a parameter.

Unconditionally returns 0.

.. _`ppc4xx_edac_opstate_init`:

ppc4xx_edac_opstate_init
========================

.. c:function:: void ppc4xx_edac_opstate_init( void)

    initialize EDAC reporting method

    :param  void:
        no arguments

.. _`ppc4xx_edac_opstate_init.description`:

Description
-----------

This routine ensures that the EDAC memory controller reporting
method is mapped to a sane value as the EDAC core defines the value
to EDAC_OPSTATE_INVAL by default. We don't call the global
opstate_init as that defaults to polling and we want interrupt as
the default.

.. _`ppc4xx_edac_init`:

ppc4xx_edac_init
================

.. c:function:: int ppc4xx_edac_init( void)

    driver/module insertion entry point

    :param  void:
        no arguments

.. _`ppc4xx_edac_init.description`:

Description
-----------

This routine is the driver/module insertion entry point. It
initializes the EDAC memory controller reporting state and
registers the driver as an OpenFirmware device tree platform
driver.

.. _`ppc4xx_edac_exit`:

ppc4xx_edac_exit
================

.. c:function:: void __exit ppc4xx_edac_exit( void)

    driver/module removal entry point

    :param  void:
        no arguments

.. _`ppc4xx_edac_exit.description`:

Description
-----------

This routine is the driver/module removal entry point. It
unregisters the driver as an OpenFirmware device tree platform
driver.

.. This file was automatic generated / don't edit.

