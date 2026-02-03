# Awesome ECS

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of Entity-Component-System (ECS) libraries and resources.

## Contents
* [ECS Libraries](#ecs-libraries)
* [Applications powered by ECS](#applications-powered-by-ecs)
  * [Game Engines](#game-engines)
  * [Graphics Engines](#graphics-engines)
  * [Physics Libraries](#physics-libraries)
* [Other Resources](#other-resources)
  * [Benchmarks](#benchmarks)
  * [Blog Posts](#blog-posts)
  * [Talks & Slides](#talks--slides)
  * [Books](#books)
  * [Tutorials](#tutorials)
  * [Lists](#lists)
  * [ETC](#etc)

> **Legend**: 🟢 Active (<1yr) · 🟡 Slow (1-2yr) · 🔴 Stale (>2yr) · 💀 Archived

## [ECS Libraries](#contents)

_Libraries and frameworks implementing the Entity-Component-System pattern._

#### C/C++

* 💀 [anax](https://github.com/miguelmartin75/anax) - Open source C++ entity system. [⭐ 463](https://github.com/miguelmartin75/anax)
* 💀 [ECS](https://github.com/redxdev/ECS) - C++ single-header entity component system library. [⭐ 480](https://github.com/redxdev/ECS)
* 🔴 [ecs.hpp](https://github.com/BlackMATov/ecs.hpp) - A single header C++14 entity component system library. [⭐ 40](https://github.com/BlackMATov/ecs.hpp)
* 🔴 [ecst](https://github.com/vittorioromeo/ecst) - Experimental C++14 multithreaded compile-time entity-compnent-system library. [⭐ 490](https://github.com/vittorioromeo/ecst)
* 🔴 [EntityFu](https://github.com/NatWeiss/EntityFu) - A simple, fast entity component system written in C++. [⭐ 86](https://github.com/NatWeiss/EntityFu)
* 🔴 [EntityPlus](https://github.com/Yelnats321/EntityPlus) - C++14 entity component system. [⭐ 191](https://github.com/Yelnats321/EntityPlus)
* 🟢 [EntityX](https://github.com/alecthomas/entityx) - Fast, type-safe C++ entity component system. [⭐ 2.3k](https://github.com/alecthomas/entityx)
* 🟢 [entt](https://github.com/skypjack/entt) - Fast and reliable entity-component system. [⭐ 12.2k](https://github.com/skypjack/entt)
* 🟢 [Flecs](https://github.com/SanderMertens/flecs) - A Multithreaded Entity Component System written for C89 & C99. [⭐ 8.0k](https://github.com/SanderMertens/flecs)
* 🟢 [Gaia-ECS](https://github.com/richardbiely/gaia-ecs) - Fast and type-safe C++17 archetype-based entity component system. [⭐ 116](https://github.com/richardbiely/gaia-ecs)
* 🔴 [Ginseng](https://github.com/apples/ginseng) - An ESC library designed for use in games. [⭐ 55](https://github.com/apples/ginseng)
* 🔴 [goomy](https://github.com/vberlier/goomy) - A tiny, experimental ECS framework. [⭐ 14](https://github.com/vberlier/goomy)
* 🔴 [Kengine](https://github.com/phisko/kengine) - Game engine with an Entity-Component-System (ECS) architecture. [⭐ 616](https://github.com/phisko/kengine)
* 🔴 [matter](https://github.com/frengels/matter) - C++17/20 ECS implementation. [⭐ 21](https://github.com/frengels/matter)
* 🟢 [mustache](https://github.com/kirillochnev/mustache) - A fast, modern C++ entity component system. [⭐ 68](https://github.com/kirillochnev/mustache)
* 🟢 [pico_ecs](https://github.com/empyreanx/pico_headers) - Single-header and cross-platform ECS. [⭐ 479](https://github.com/empyreanx/pico_headers)
* 🟢 [WickedEngine's ECS](https://github.com/turanszkij/WickedEngine/blob/master/WickedEngine/wiECS.h) - WickedEngine's ECS implementation. [⭐ 6.8k](https://github.com/turanszkij/WickedEngine)

#### C#

* 🟢 [Arch](https://github.com/genaray/Arch) - A high-performance Archetype & Chunks Entity Component System for game development and data-oriented programming. [⭐ 1.6k](https://github.com/genaray/Arch)
* 🔴 [DefaultEcs](https://github.com/Doraku/DefaultEcs) - ECS for syntax and usage simplicity with maximum performance. [⭐ 746](https://github.com/Doraku/DefaultEcs)
* 🟢 [DragonECS](https://github.com/DCFApixels/DragonECS) - ECS for Unity and .NET. [⭐ 291](https://github.com/DCFApixels/DragonECS)
* 🔴 [Entitas](https://github.com/sschmid/Entitas) - The Entity Component System Framework for C# and Unity. [⭐ 7.6k](https://github.com/sschmid/Entitas)
* 🟢 [Fennecs](https://github.com/outfox/fennecs) - ... the tiny, tiny, high-energy Entity-Component System! [⭐ 407](https://github.com/outfox/fennecs)
* 🟢 [Frent](https://github.com/itsBuggingMe/Frent) - Data oriented ECF with an ECS api for C#, Godot, and Unity. [⭐ 154](https://github.com/itsBuggingMe/Frent)
* 🟢 [Friflo Engine ECS](https://github.com/friflo/Friflo.Engine.ECS) - ECS for .NET with focus on performance, cache locality and DX. [⭐ 525](https://github.com/friflo/Friflo.Engine.ECS)
* 🔴 [LeoEcsLite](https://github.com/LeoECSCommunity/ecslite) - Lightweight C# Entity Component System framework. [⭐ 60](https://github.com/LeoECSCommunity/ecslite)
* 🟢 [Massive ECS](https://github.com/nilpunch/massive-ecs) - Bitset-based ECS with rollbacks. C# library and Unity package. [⭐ 171](https://github.com/nilpunch/massive-ecs)
* 🟢 [ME.BECS](https://github.com/chromealex/ME.BECS) - ECS for Unity with full game state automatic rollbacks. [⭐ 241](https://github.com/chromealex/ME.BECS)
* 🟢 [Morpeh](https://github.com/scellecs/morpeh) - ECS Framework for Unity Game Engine and .NET Platform. [⭐ 630](https://github.com/scellecs/morpeh)
* 🟢 [Static ECS](https://github.com/Felid-Force-Studios/StaticEcs) - C# Hierarchical Inverted Bitmap ECS framework. [⭐ 136](https://github.com/Felid-Force-Studios/StaticEcs)
* 🟢 [Svelto.ECS](https://github.com/sebas77/Svelto.ECS) - Lightweight data oriented entity component system framework. [⭐ 1.4k](https://github.com/sebas77/Svelto.ECS)
* 🟢 [TinyEcs](https://github.com/andreakarasho/TinyEcs) - A tiny bevy-like archetype-style ECS library for dotnet. [⭐ 134](https://github.com/andreakarasho/TinyEcs)

#### Common Lisp

* 🔴 [beast](https://github.com/sjl/beast) - Basic Entity/Aspect/System Toolkit. [⭐ 30](https://github.com/sjl/beast)
* 🔴 [cl-ecs](https://github.com/bit-phlippers/cl-ecs) - An implementation of the Entity-Component-System pattern mostly used in game development. [⭐ 8](https://github.com/bit-phlippers/cl-ecs)
* [cl-fast-ecs](https://gitlab.com/lockie/cl-fast-ecs) - Blazingly fast Entity-Component-System microframework. [gitlab](https://gitlab.com/lockie/cl-fast-ecs)

#### Dart

* 🔴 [Fast ECS](https://github.com/QiXi/fast_ecs) - Simple and fast Entity-Component-System (ECS) library written in Dart. [⭐ 17](https://github.com/QiXi/fast_ecs)

#### Elixir

* 🟡 [ECSx](https://github.com/ecsx-framework/ECSx) - An ECS framework for Elixir. [⭐ 258](https://github.com/ecsx-framework/ECSx)

#### Python

* 🟢 [esper](https://github.com/benmoran56/esper) - A lightweight Entity System for Python. [⭐ 669](https://github.com/benmoran56/esper)

#### Rust

* 🟢 [bevy_ecs](https://github.com/bevyengine/bevy/tree/main/crates/bevy_ecs) - Simple to use, ergonomic, fast, massively parallel, opinionated, and featureful written in Rust. [⭐ 44.5k](https://github.com/bevyengine/bevy)
* 🟢 [hecs](https://github.com/Ralith/hecs) - High-performance, minimalist entity-component-system. [⭐ 1.2k](https://github.com/Ralith/hecs)
* 🔴 [legion](https://github.com/amethyst/legion) - High performance Rust ECS library. [⭐ 1.7k](https://github.com/amethyst/legion)
* 🟢 [shipyard](https://github.com/leudz/shipyard) - Entity Component System written in Rust. [⭐ 834](https://github.com/leudz/shipyard)
* 🟡 [specs](https://github.com/amethyst/specs) - Parallel entity component system written in Rust. [⭐ 2.6k](https://github.com/amethyst/specs)

#### Go

* 🟢 [Ark](https://github.com/mlange-42/ark) - An archetype-based Entity Component System for Go. [⭐ 209](https://github.com/mlange-42/ark)
* 🔴 [ecs](https://github.com/EngoEngine/ecs) - A Go-implementation of the Entity-Component-System paradigm. [⭐ 331](https://github.com/EngoEngine/ecs)

#### Lua

* 🟡 [Concord](https://github.com/Keyslam-Group/Concord) - A feature-complete ECS library. [⭐ 302](https://github.com/Keyslam-Group/Concord)
* 🔴 [ECS Lua](https://github.com/nidorx/ecs-lua) - A fast and easy to use ECS engine for game development. [⭐ 224](https://github.com/nidorx/ecs-lua)
* 🟢 [evolved.lua](https://github.com/BlackMATov/evolved.lua) - Evolved ECS (Entity-Component-System) for Lua. [⭐ 171](https://github.com/BlackMATov/evolved.lua)
* 🔴 [Nata](https://github.com/tesselode/nata) - Entity management for Lua. [⭐ 51](https://github.com/tesselode/nata)
* 🔴 [tiny-ecs](https://github.com/bakpakin/tiny-ecs) - Entity Component System for Lua that's simple, flexible, and useful. [⭐ 774](https://github.com/bakpakin/tiny-ecs)

#### Java

* 🔴 [Artemis-odb](https://github.com/junkdog/artemis-odb) - A continuation of the popular Artemis ECS framework. [⭐ 825](https://github.com/junkdog/artemis-odb)

#### Julia

* 🟢 [Ark.jl](https://github.com/ark-ecs/Ark.jl) - An archetype-based Entity Component System (ECS) for Julia. It is a port of the Go ECS Ark. [⭐ 52](https://github.com/ark-ecs/Ark.jl)

#### Kotlin

* 🟢 [Fleks](https://github.com/Quillraven/Fleks) - Fast, lightweight, multi-platform entity component system in Kotlin. [⭐ 243](https://github.com/Quillraven/Fleks)

#### JavaScript / TypeScript

* 🟢 [becsy](https://github.com/LastOliveGames/becsy) - A multithreaded Entity Component System (ECS) for TypeScript and JavaScript, inspired by ECSY and bitecs. [⭐ 284](https://github.com/LastOliveGames/becsy)
* 🟢 [bitECS](https://github.com/NateTheGreatt/bitECS) - Functional, minimal, data-oriented, ultra-high performance ECS library. [⭐ 1.3k](https://github.com/NateTheGreatt/bitECS)
* 💀 [ECSY](https://github.com/ecsyjs/ecsy) - Entity Component System for javascript. [⭐ 1.1k](https://github.com/ecsyjs/ecsy)
* 🔴 [miniplex](https://github.com/hmans/miniplex) - The gentle game entity manager, focused on ease of use and developer experience. [⭐ 977](https://github.com/hmans/miniplex)
* 🟡 [Thyseus](https://github.com/JaimeGensler/thyseus) - An archetypal Entity Component System, built entirely in Typescript. [⭐ 86](https://github.com/JaimeGensler/thyseus)

#### Zig

* 🟢 [Comptime ECS](https://github.com/Very-Blank/Ecs) - Comptime-defined ECS implementation in Zig. [⭐ 4](https://github.com/Very-Blank/Ecs)
* 🟢 [knoedel](https://github.com/Lommix/knoedel) - Data oriented application framework written in Zig (ECS). [⭐ 27](https://github.com/Lommix/knoedel)
* 🟡 [mach-ecs](https://github.com/hexops-graveyard/mach-ecs) - Entity Component System from first-principles designed for Zig. [⭐ 35](https://github.com/hexops-graveyard/mach-ecs)
* 🟢 [ZCS](https://github.com/Games-by-Mason/ZCS) - An archetype based entity component system written in Zig. [⭐ 145](https://github.com/Games-by-Mason/ZCS)
* 🟢 [Zig ECS](https://github.com/prime31/zig-ecs) - A Zig port of the fantasic Entt. [⭐ 390](https://github.com/prime31/zig-ecs)

#### Haskell

* 🟢 [apecs](https://github.com/jonascarpay/apecs) - A fast, extensible, type driven Haskell ECS framework for games. [⭐ 407](https://github.com/jonascarpay/apecs)

## [Applications powered by ECS](#contents)

### [Game Engines](#contents)

_Game engines built on ECS architecture._

#### C++

* 🟢 [crown](https://github.com/dbartolini/crown) - General purpose data-driven game engine. [⭐ 27](https://github.com/dbartolini/crown)
* 🔴 [Engine](https://github.com/Shervanator/Engine) - Basic cross-platform 3D game engine. [⭐ 301](https://github.com/Shervanator/Engine)
* 🟢 [halley](https://github.com/amzeratul/halley) - A lightweight game engine written in modern C++. [⭐ 3.8k](https://github.com/amzeratul/halley)
* 🔴 [igneous](https://github.com/MissingBitStudios/igneous) - Open source game engine written in C++. [⭐ 51](https://github.com/MissingBitStudios/igneous)
* 🔴 [kengine](https://github.com/phisko/kengine) - Game engine focused on ease-of-use, runtime extensibility and compile-time type safety. [⭐ 616](https://github.com/phisko/kengine)
* 🟢 [Lina Engine](https://github.com/inanevin/LinaEngine) - Modular, tiny and fast C++ game engine, aimed to develop 3D desktop games. [⭐ 889](https://github.com/inanevin/LinaEngine)
* 🟢 [Lumos](https://github.com/jmorton06/Lumos) - Cross-Platform C++ 2D/3D game engine. [⭐ 1.5k](https://github.com/jmorton06/Lumos)
* 🟡 [MxEngine](https://github.com/asc-community/MxEngine) - C++ open source 3D game engine. [⭐ 1.2k](https://github.com/asc-community/MxEngine)
* 🟢 [Nazara Engine](https://github.com/NazaraEngine/NazaraEngine) - Cross-platform framework aimed at real-time applications requiring audio, 2D and 3D real-time rendering, network and more. [⭐ 809](https://github.com/NazaraEngine/NazaraEngine)
* 🟢 [nebula](https://github.com/gscept/nebula) - Open-source and free-to-use modern C++ game engine. [⭐ 1.0k](https://github.com/gscept/nebula)
* 💀 [shiva](https://github.com/Milerius/shiva) - Modern Cross-Platform C++ Engine with modularity. [⭐ 159](https://github.com/Milerius/shiva)
* 🔴 [Sparky](https://github.com/TheCherno/Sparky) - Cross-Platform High Performance 2D/3D game engine. [⭐ 1.2k](https://github.com/TheCherno/Sparky)
* 🟢 [supernova](https://github.com/supernovaengine/supernova) - Game engine for 2D and 3D projects with ECS and data-oriented design. [⭐ 376](https://github.com/supernovaengine/supernova)
* 🔴 [Usagi](https://github.com/vitei/Usagi) - Hierarchical component entity system based game engine. [⭐ 53](https://github.com/vitei/Usagi)
* 🟢 [WickedEngine](https://github.com/turanszkij/WickedEngine) - 3D engine with modern graphics. [⭐ 6.8k](https://github.com/turanszkij/WickedEngine)

#### Go

* 🟡 [Engo](https://github.com/EngoEngine/engo) - A cross-platform game engine written in Go following an interpretation of the Entity Component System paradigm. [⭐ 1.8k](https://github.com/EngoEngine/engo)

#### Rust

* 🟡 [Ambient](https://github.com/AmbientRun/Ambient) - The multiplayer game engine. [⭐ 3.9k](https://github.com/AmbientRun/Ambient)
* 💀 [Amethyst](https://github.com/amethyst/amethyst) - Data-oriented and data-driven game engine written in Rust. [⭐ 8.0k](https://github.com/amethyst/amethyst)
* 🟢 [Bevy](https://github.com/bevyengine/bevy) - A refreshingly simple data-driven game engine built in Rust. [⭐ 44.5k](https://github.com/bevyengine/bevy)
* 🟢 [Bones](https://github.com/fishfolk/bones) - An easy-to-use game engine for making real games. [⭐ 289](https://github.com/fishfolk/bones)

#### Zig

* 🟢 [mach](https://github.com/hexops/mach) - Game engine & graphics toolkit for building high-performance, truly cross-platform, robust & modular games, visualizations, and desktop/mobile GUI apps. [⭐ 4.6k](https://github.com/hexops/mach)

### [Graphics Engines](#contents)

_Graphics and rendering engines using ECS._

#### C++

* 🔴 [bs::framework](https://github.com/GameFoundry/bsf) - Modern C++14 library for the development of real-time graphical applications. [⭐ 1.8k](https://github.com/GameFoundry/bsf)
* 🟢 [The Forge](https://github.com/ConfettiFX/The-Forge) - Cross-Platform Rendering Framework with support for PC Windows, Linux, Ray Tracing, macOS/iOS, Android, XBOX, PS4, PS5, Switch, Quest 2. [⭐ 5.5k](https://github.com/ConfettiFX/The-Forge)

### [Physics Libraries](#contents)

_Physics simulation libraries organized as ECS._

#### C++

* 🟢 [edyn](https://github.com/xissburg/edyn) - A real-time physics engine organized as an ECS. [⭐ 746](https://github.com/xissburg/edyn)

## [Other Resources](#contents)

### [Benchmarks](#contents)

_Performance benchmarks comparing ECS frameworks._

* 🔴 [CSharpECSComparison](https://github.com/Chillu1/CSharpECSComparison) - Benchmarks of common ECS Frameworks for C#. [⭐ 53](https://github.com/Chillu1/CSharpECSComparison)
* 🟢 [ECS C# Benchmark](https://github.com/Doraku/Ecs.CSharp.Benchmark) - Benchmarks of the main ECS Frameworks for: C#. [⭐ 174](https://github.com/Doraku/Ecs.CSharp.Benchmark)
* 🟢 [ECS C# Benchmark - Common uses-cases](https://github.com/friflo/ECS.CSharp.Benchmark-common-use-cases) - Benchmark many common use cases in the simplest and most performant variant. [⭐ 43](https://github.com/friflo/ECS.CSharp.Benchmark-common-use-cases)
* 🟡 [ecs_benchmark](https://github.com/abeimler/ecs_benchmark) - Benchmarks of common ECS (Entity-Component-System)-Frameworks in C/C++. [⭐ 280](https://github.com/abeimler/ecs_benchmark)
* 🟢 [Lua ECS Library Benchmark](https://github.com/jeffzi/lua-ecs-benchmark) - Benchmarks of common ECS Frameworks in Lua. [⭐ 6](https://github.com/jeffzi/lua-ecs-benchmark)

### [Blog Posts](#contents)

_Articles and blog posts about ECS and data-oriented design._

* [Building an ECS](https://ajmmertens.medium.com/building-an-ecs-1-where-are-my-entities-and-components-63d07c7da742)
* [Data-oriented design](http://gamesfromwithin.com/category/data-oriented-design)
* [ECS back and forth](https://skypjack.github.io/2019-02-14-ecs-baf-part-1/)
* [Entity Systems are the future of MMOG development](https://t-machine.org/index.php/2007/09/03/entity-systems-are-the-future-of-mmog-development-part-1/)
* [Let's build an Entity Component System from scratch](https://devlog.hexops.com/2022/lets-build-ecs-part-1/)
* [Overview of ECS variants & definitions](https://gist.github.com/LearnCocos2D/77f0ced228292676689f)
* [Seba's Lab](https://www.sebaslab.com/)
* [Systems Interaction in Entity-Component-System (events)](https://medium.com/@ben.rasooli/systems-interaction-in-entity-component-system-events-4a050153c8ac)
* [Understand data-oriented design](https://learn.unity.com/tutorial/part-1-understand-data-oriented-design)
* [Unity ECS series](https://gametorrahod.com/tag/unity-dots/)
* [WickedEngine's ECS implementation](https://wickedengine.net/2019/09/entity-component-system/)

### [Talks & Slides](#contents)

_Conference talks and presentations about ECS._

* [Codestar 2018 ECS - A Different Approach to Game Development](https://www.youtube.com/watch?v=lt4eL4RSx7k)
* [CppCon 2014: Mike Acton "Data-Oriented Design and C++"](https://youtu.be/rX0ItVEVjHc)
* [CppCon 2018: Stoyan Nikolov “OOP Is Dead, Long Live Data-oriented Design”](https://youtu.be/yy8jQgmhbAU)
* [Data Oriented Design Resources](http://aras-p.info/texts/files/2018Academy%20-%20ECS-DoD.pdf)
* [Data Oriented GUI in Rust](https://www.youtube.com/watch?v=4YTfxresvS8)
* [GDC 2018: Unity at GDC - A Data Oriented Approach to Using Component Systems](https://youtu.be/p65Yt20pw0g)
* [Is There More to Game Architecture than ECS](https://www.youtube.com/watch?v=JxI3Eu5DPwE) - Bob Nystrom (Roguelike Celebration 2018)
* [itCppCon19: ECS back and forth](https://youtu.be/WB5bRKKGRUk)
* [Meeting C++ 2018: Data oriented design in practice](https://youtu.be/NWMx1Q66c14)
* [Unite 2018: C# Job System + ECS usage and demo with Intel](https://www.youtube.com/watch?v=fp1D45hhVEM)

### [Books](#contents)

_Books on ECS and data-oriented design._

* [Data-Oriented Design](http://www.dataorienteddesign.com/dodbook/)

### [Tutorials](#contents)

_Tutorial series for learning ECS._

* [Starting a new 2D platformer with ECS](https://www.youtube.com/playlist?list=PLWtPciJ1UMuAoCq8NAw8J-n387U4QHFBW)

### [Lists](#contents)

_Related curated lists._

* [Entity Component System & Data Oriented Design](https://github.com/dbartolini/data-oriented-design)

### [ETC](#contents)

_Other ECS-related resources._

* [Entity Component Systems FAQ](https://github.com/SanderMertens/ecs-faq)
* [Entity Systems Wiki](http://entity-systems.wikidot.com/)

## [Contributing](#contents)

Contributions are very welcome! Please read the [contribution guidelines](CONTRIBUTING.md) first. Also, please feel free to report any error.

## [License](#contents)

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)
