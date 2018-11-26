.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_debugfs.c

.. _`amdgpu_debugfs_add_files`:

amdgpu_debugfs_add_files
========================

.. c:function:: int amdgpu_debugfs_add_files(struct amdgpu_device *adev, const struct drm_info_list *files, unsigned nfiles)

    Add simple debugfs entries

    :param adev:
        Device to attach debugfs entries to
    :type adev: struct amdgpu_device \*

    :param files:
        Array of function callbacks that respond to reads
    :type files: const struct drm_info_list \*

    :param nfiles:
        Number of callbacks to register
    :type nfiles: unsigned

.. _`amdgpu_debugfs_process_reg_op`:

amdgpu_debugfs_process_reg_op
=============================

.. c:function:: int amdgpu_debugfs_process_reg_op(bool read, struct file *f, char __user *buf, size_t size, loff_t *pos)

    Handle MMIO register reads/writes

    :param read:
        True if reading
    :type read: bool

    :param f:
        open file handle
    :type f: struct file \*

    :param buf:
        User buffer to write/read to
    :type buf: char __user \*

    :param size:
        Number of bytes to write/read
    :type size: size_t

    :param pos:
        Offset to seek to
    :type pos: loff_t \*

.. _`amdgpu_debugfs_process_reg_op.description`:

Description
-----------

This debugfs entry has special meaning on the offset being sought.

.. _`amdgpu_debugfs_process_reg_op.bit-62`:

Bit 62
------

Indicates a GRBM bank switch is needed

.. _`amdgpu_debugfs_process_reg_op.bit-61`:

Bit 61
------

Indicates a SRBM bank switch is needed (implies bit 62 is
zero)
Bits 24..33: The SE or ME selector if needed
Bits 34..43: The SH (or SA) or PIPE selector if needed
Bits 44..53: The INSTANCE (or CU/WGP) or QUEUE selector if needed

.. _`amdgpu_debugfs_process_reg_op.bit-23`:

Bit 23
------

Indicates that the PM power gating lock should be held
This is necessary to read registers that might be
unreliable during a power gating transistion.

The lower bits are the BYTE offset of the register to read.  This
allows reading multiple registers in a single call and having
the returned size reflect that.

.. _`amdgpu_debugfs_regs_read`:

amdgpu_debugfs_regs_read
========================

.. c:function:: ssize_t amdgpu_debugfs_regs_read(struct file *f, char __user *buf, size_t size, loff_t *pos)

    Callback for reading MMIO registers

    :param f:
        *undescribed*
    :type f: struct file \*

    :param buf:
        *undescribed*
    :type buf: char __user \*

    :param size:
        *undescribed*
    :type size: size_t

    :param pos:
        *undescribed*
    :type pos: loff_t \*

.. _`amdgpu_debugfs_regs_write`:

amdgpu_debugfs_regs_write
=========================

.. c:function:: ssize_t amdgpu_debugfs_regs_write(struct file *f, const char __user *buf, size_t size, loff_t *pos)

    Callback for writing MMIO registers

    :param f:
        *undescribed*
    :type f: struct file \*

    :param buf:
        *undescribed*
    :type buf: const char __user \*

    :param size:
        *undescribed*
    :type size: size_t

    :param pos:
        *undescribed*
    :type pos: loff_t \*

.. _`amdgpu_debugfs_regs_pcie_read`:

amdgpu_debugfs_regs_pcie_read
=============================

.. c:function:: ssize_t amdgpu_debugfs_regs_pcie_read(struct file *f, char __user *buf, size_t size, loff_t *pos)

    Read from a PCIE register

    :param f:
        open file handle
    :type f: struct file \*

    :param buf:
        User buffer to store read data in
    :type buf: char __user \*

    :param size:
        Number of bytes to read
    :type size: size_t

    :param pos:
        Offset to seek to
    :type pos: loff_t \*

.. _`amdgpu_debugfs_regs_pcie_read.description`:

Description
-----------

The lower bits are the BYTE offset of the register to read.  This
allows reading multiple registers in a single call and having
the returned size reflect that.

.. _`amdgpu_debugfs_regs_pcie_write`:

amdgpu_debugfs_regs_pcie_write
==============================

.. c:function:: ssize_t amdgpu_debugfs_regs_pcie_write(struct file *f, const char __user *buf, size_t size, loff_t *pos)

    Write to a PCIE register

    :param f:
        open file handle
    :type f: struct file \*

    :param buf:
        User buffer to write data from
    :type buf: const char __user \*

    :param size:
        Number of bytes to write
    :type size: size_t

    :param pos:
        Offset to seek to
    :type pos: loff_t \*

.. _`amdgpu_debugfs_regs_pcie_write.description`:

Description
-----------

The lower bits are the BYTE offset of the register to write.  This
allows writing multiple registers in a single call and having
the returned size reflect that.

.. _`amdgpu_debugfs_regs_didt_read`:

amdgpu_debugfs_regs_didt_read
=============================

.. c:function:: ssize_t amdgpu_debugfs_regs_didt_read(struct file *f, char __user *buf, size_t size, loff_t *pos)

    Read from a DIDT register

    :param f:
        open file handle
    :type f: struct file \*

    :param buf:
        User buffer to store read data in
    :type buf: char __user \*

    :param size:
        Number of bytes to read
    :type size: size_t

    :param pos:
        Offset to seek to
    :type pos: loff_t \*

.. _`amdgpu_debugfs_regs_didt_read.description`:

Description
-----------

The lower bits are the BYTE offset of the register to read.  This
allows reading multiple registers in a single call and having
the returned size reflect that.

.. _`amdgpu_debugfs_regs_didt_write`:

amdgpu_debugfs_regs_didt_write
==============================

.. c:function:: ssize_t amdgpu_debugfs_regs_didt_write(struct file *f, const char __user *buf, size_t size, loff_t *pos)

    Write to a DIDT register

    :param f:
        open file handle
    :type f: struct file \*

    :param buf:
        User buffer to write data from
    :type buf: const char __user \*

    :param size:
        Number of bytes to write
    :type size: size_t

    :param pos:
        Offset to seek to
    :type pos: loff_t \*

.. _`amdgpu_debugfs_regs_didt_write.description`:

Description
-----------

The lower bits are the BYTE offset of the register to write.  This
allows writing multiple registers in a single call and having
the returned size reflect that.

.. _`amdgpu_debugfs_regs_smc_read`:

amdgpu_debugfs_regs_smc_read
============================

.. c:function:: ssize_t amdgpu_debugfs_regs_smc_read(struct file *f, char __user *buf, size_t size, loff_t *pos)

    Read from a SMC register

    :param f:
        open file handle
    :type f: struct file \*

    :param buf:
        User buffer to store read data in
    :type buf: char __user \*

    :param size:
        Number of bytes to read
    :type size: size_t

    :param pos:
        Offset to seek to
    :type pos: loff_t \*

.. _`amdgpu_debugfs_regs_smc_read.description`:

Description
-----------

The lower bits are the BYTE offset of the register to read.  This
allows reading multiple registers in a single call and having
the returned size reflect that.

.. _`amdgpu_debugfs_regs_smc_write`:

amdgpu_debugfs_regs_smc_write
=============================

.. c:function:: ssize_t amdgpu_debugfs_regs_smc_write(struct file *f, const char __user *buf, size_t size, loff_t *pos)

    Write to a SMC register

    :param f:
        open file handle
    :type f: struct file \*

    :param buf:
        User buffer to write data from
    :type buf: const char __user \*

    :param size:
        Number of bytes to write
    :type size: size_t

    :param pos:
        Offset to seek to
    :type pos: loff_t \*

.. _`amdgpu_debugfs_regs_smc_write.description`:

Description
-----------

The lower bits are the BYTE offset of the register to write.  This
allows writing multiple registers in a single call and having
the returned size reflect that.

.. _`amdgpu_debugfs_gca_config_read`:

amdgpu_debugfs_gca_config_read
==============================

.. c:function:: ssize_t amdgpu_debugfs_gca_config_read(struct file *f, char __user *buf, size_t size, loff_t *pos)

    Read from gfx config data

    :param f:
        open file handle
    :type f: struct file \*

    :param buf:
        User buffer to store read data in
    :type buf: char __user \*

    :param size:
        Number of bytes to read
    :type size: size_t

    :param pos:
        Offset to seek to
    :type pos: loff_t \*

.. _`amdgpu_debugfs_gca_config_read.description`:

Description
-----------

This file is used to access configuration data in a somewhat
stable fashion.  The format is a series of DWORDs with the first
indicating which revision it is.  New content is appended to the
end so that older software can still read the data.

.. _`amdgpu_debugfs_sensor_read`:

amdgpu_debugfs_sensor_read
==========================

.. c:function:: ssize_t amdgpu_debugfs_sensor_read(struct file *f, char __user *buf, size_t size, loff_t *pos)

    Read from the powerplay sensors

    :param f:
        open file handle
    :type f: struct file \*

    :param buf:
        User buffer to store read data in
    :type buf: char __user \*

    :param size:
        Number of bytes to read
    :type size: size_t

    :param pos:
        Offset to seek to
    :type pos: loff_t \*

.. _`amdgpu_debugfs_sensor_read.description`:

Description
-----------

The offset is treated as the BYTE address of one of the sensors
enumerated in amd/include/kgd_pp_interface.h under the
'amd_pp_sensors' enumeration.  For instance to read the UVD VCLK
you would use the offset 3 \* 4 = 12.

.. _`amdgpu_debugfs_regs_init`:

amdgpu_debugfs_regs_init
========================

.. c:function:: int amdgpu_debugfs_regs_init(struct amdgpu_device *adev)

    Initialize debugfs entries that provide register access.

    :param adev:
        The device to attach the debugfs entries to
    :type adev: struct amdgpu_device \*

.. This file was automatic generated / don't edit.

