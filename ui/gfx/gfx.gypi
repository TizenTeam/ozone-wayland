# Copyright 2014 Intel Corporation. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
{
  'dependencies': [
    '<(DEPTH)/ui/gfx/gfx.gyp:gfx',
  ],
  'sources': [
    'ozone_display.h',
    'ozone_display.cc',
    'surface_factory_wayland.cc',
    'surface_factory_wayland.h',
    'vsync_provider_wayland.cc',
    'vsync_provider_wayland.h',
   ],
}
