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
  * [References](#references)
* [Contributing](#contributing)

> **Legend**: 🟢 commit within 1 yr · 🟡 commit within 3 yr · 💀 archived · ⭐ GitHub stars as of 2026-10-12. Software entries are ordered by stars; inactive entries (archived, or no commits for 3+ years) are folded at the end of each software category. Other resources keep their existing order.

## [ECS Libraries](#contents)

_Libraries and frameworks implementing the Entity-Component-System pattern._

#### C/C++

* 🟢 [entt](https://github.com/skypjack/entt) - Fast and reliable entity-component system. [⭐ 13.2k](https://github.com/skypjack/entt)
* 🟢 [Flecs](https://github.com/SanderMertens/flecs) - A Multithreaded Entity Component System written for C89 & C99. [⭐ 8.7k](https://github.com/SanderMertens/flecs)
* 🟢 [WickedEngine's ECS](https://github.com/turanszkij/WickedEngine/blob/master/WickedEngine/wiECS.h) - WickedEngine's ECS implementation. [⭐ 7.3k](https://github.com/turanszkij/WickedEngine)
* 🟡 [EntityX](https://github.com/alecthomas/entityx) - Fast, type-safe C++ entity component system. [⭐ 2.3k](https://github.com/alecthomas/entityx)
* 🟢 [pico_ecs](https://github.com/empyreanx/pico_headers) - Single-header and cross-platform ECS. [⭐ 564](https://github.com/empyreanx/pico_headers)
* 🟢 [Gaia-ECS](https://github.com/richardbiely/gaia-ecs) - Fast and type-safe C++17 archetype-based entity component system. [⭐ 134](https://github.com/richardbiely/gaia-ecs)
* 🟢 [mustache](https://github.com/kirillochnev/mustache) - A fast, modern C++ entity component system. [⭐ 78](https://github.com/kirillochnev/mustache)

#### C#

* 🟢 [Arch](https://github.com/genaray/Arch) - A high-performance Archetype & Chunks Entity Component System for game development and data-oriented programming. [⭐ 1.8k](https://github.com/genaray/Arch)
* 🟡 [Svelto.ECS](https://github.com/sebas77/Svelto.ECS) - Lightweight data oriented entity component system framework. [⭐ 1.4k](https://github.com/sebas77/Svelto.ECS)
* 🟢 [Friflo Engine ECS](https://github.com/friflo/Friflo.Engine.ECS) - ECS for .NET with focus on performance, cache locality and DX. [⭐ 785](https://github.com/friflo/Friflo.Engine.ECS)
* 🟡 [Morpeh](https://github.com/scellecs/morpeh) - ECS Framework for Unity Game Engine and .NET Platform. [⭐ 672](https://github.com/scellecs/morpeh)
* 🟢 [Fennecs](https://github.com/outfox/fennecs) - ... the tiny, tiny, high-energy Entity-Component System! [⭐ 470](https://github.com/outfox/fennecs)
* 🟢 [DragonECS](https://github.com/DCFApixels/DragonECS) - ECS for Unity and .NET. [⭐ 343](https://github.com/DCFApixels/DragonECS)
* 🟢 [ME.BECS](https://github.com/chromealex/ME.BECS) - ECS for Unity with full game state automatic rollbacks. [⭐ 257](https://github.com/chromealex/ME.BECS)
* 🟢 [Massive ECS](https://github.com/nilpunch/massive-ecs) - Bitset-based ECS with rollbacks. C# library and Unity package. [⭐ 224](https://github.com/nilpunch/massive-ecs)
* 🟢 [Static ECS](https://github.com/Felid-Force-Studios/StaticEcs) - C# Hierarchical Inverted Bitmap ECS framework. [⭐ 211](https://github.com/Felid-Force-Studios/StaticEcs)
* 🟢 [Frent](https://github.com/itsBuggingMe/Frent) - Data oriented ECF with an ECS api for C#, Godot, and Unity. [⭐ 187](https://github.com/itsBuggingMe/Frent)
* 🟢 [TinyEcs](https://github.com/andreakarasho/TinyEcs) - A tiny bevy-like archetype-style ECS library for dotnet. [⭐ 153](https://github.com/andreakarasho/TinyEcs)

#### Common Lisp

* [cl-fast-ecs](https://gitlab.com/lockie/cl-fast-ecs) - Blazingly fast Entity-Component-System microframework. [[gitlab](https://gitlab.com/lockie/cl-fast-ecs)]

#### Elixir

* 🟡 [ECSx](https://github.com/ecsx-framework/ECSx) - An ECS framework for Elixir. [⭐ 270](https://github.com/ecsx-framework/ECSx)

#### Python

* 🟢 [esper](https://github.com/benmoran56/esper) - A lightweight Entity System for Python. [⭐ 703](https://github.com/benmoran56/esper)

#### Rust

* 🟢 [bevy_ecs](https://github.com/bevyengine/bevy/tree/main/crates/bevy_ecs) - Simple to use, ergonomic, fast, massively parallel, opinionated, and featureful written in Rust. [⭐ 48.9k](https://github.com/bevyengine/bevy)
* 🟡 [specs](https://github.com/amethyst/specs) - Parallel entity component system written in Rust. [⭐ 2.6k](https://github.com/amethyst/specs)
* 🟢 [hecs](https://github.com/Ralith/hecs) - High-performance, minimalist entity-component-system. [⭐ 1.4k](https://github.com/Ralith/hecs)
* 🟢 [shipyard](https://github.com/leudz/shipyard) - Entity Component System written in Rust. [⭐ 891](https://github.com/leudz/shipyard)

#### Go

* 🟡 [ecs](https://github.com/EngoEngine/ecs) - A Go-implementation of the Entity-Component-System paradigm. [⭐ 338](https://github.com/EngoEngine/ecs)
* 🟢 [Ark](https://github.com/mlange-42/ark) - An archetype-based Entity Component System for Go. [⭐ 302](https://github.com/mlange-42/ark)

#### Lua

* 🟢 [Concord](https://github.com/Concord-Studio/Concord) - A feature-complete ECS library. [⭐ 326](https://github.com/Keyslam-Group/Concord)
* 🟢 [evolved.lua](https://github.com/BlackMATov/evolved.lua) - Evolved ECS (Entity-Component-System) for Lua. [⭐ 224](https://github.com/BlackMATov/evolved.lua)

#### Julia

* 🟢 [Ark.jl](https://github.com/ark-ecs/Ark.jl) - An archetype-based Entity Component System (ECS) for Julia. It is a port of the Go ECS Ark. [⭐ 84](https://github.com/ark-ecs/Ark.jl)

#### Kotlin

* 🟢 [Fleks](https://github.com/Quillraven/Fleks) - Fast, lightweight, multi-platform entity component system in Kotlin. [⭐ 270](https://github.com/Quillraven/Fleks)

#### JavaScript / TypeScript

* 🟢 [bitECS](https://github.com/NateTheGreatt/bitECS) - Functional, minimal, data-oriented, ultra-high performance ECS library. [⭐ 1.5k](https://github.com/NateTheGreatt/bitECS)
* 🟢 [miniplex](https://github.com/hmans/miniplex) - The gentle game entity manager, focused on ease of use and developer experience. [⭐ 1.1k](https://github.com/hmans/miniplex)
* 🟢 [becsy](https://github.com/LastOliveGames/becsy) - A multithreaded Entity Component System (ECS) for TypeScript and JavaScript, inspired by ECSY and bitecs. [⭐ 298](https://github.com/LastOliveGames/becsy)
* 🟡 [Thyseus](https://github.com/JaimeGensler/thyseus) - An archetypal Entity Component System, built entirely in Typescript. [⭐ 86](https://github.com/JaimeGensler/thyseus)
* 🟢 [Woven-ECS](https://woven-ecs.dev/) - A multithreaded ECS framework for TypeScript aimed at collaborative browser applications. [⭐ 12](https://github.com/WillH0lt/woven-ecs)

#### Zig

* 🟢 [Zig ECS](https://github.com/prime31/zig-ecs) - A Zig port of the fantasic Entt. [⭐ 431](https://github.com/prime31/zig-ecs)
* 🟢 [ZCS](https://github.com/Games-by-Mason/ZCS) - An archetype based entity component system written in Zig. [⭐ 151](https://github.com/Games-by-Mason/ZCS)
* 🟢 [knoedel](https://github.com/Lommix/knoedel) - Data oriented application framework written in Zig (ECS). [⭐ 47](https://github.com/Lommix/knoedel)
* 🟡 [mach-ecs](https://github.com/hexops-graveyard/mach-ecs) - Entity Component System from first-principles designed for Zig. [⭐ 34](https://github.com/hexops-graveyard/mach-ecs)
* 🟢 [Comptime ECS](https://github.com/Very-Blank/Ecs) - Comptime-defined ECS implementation in Zig. [⭐ 4](https://github.com/Very-Blank/Ecs)

#### Haskell

* 🟢 [apecs](https://github.com/jonascarpay/apecs) - A fast, extensible, type driven Haskell ECS framework for games. [⭐ 425](https://github.com/jonascarpay/apecs)

<details>
<summary>Inactive (22): archived or no commits for 3+ years</summary>

* [Entitas](https://github.com/sschmid/Entitas) - The Entity Component System Framework for C# and Unity. [⭐ 7.7k](https://github.com/sschmid/Entitas) · last commit 2023
* [legion](https://github.com/amethyst/legion) - High performance Rust ECS library. [⭐ 1.7k](https://github.com/amethyst/legion) · last commit 2021
* 💀 [ECSY](https://github.com/ecsyjs/ecsy) - Entity Component System for javascript. [⭐ 1.2k](https://github.com/ecsyjs/ecsy) · last commit 2025
* [Artemis-odb](https://github.com/junkdog/artemis-odb) - A continuation of the popular Artemis ECS framework. [⭐ 832](https://github.com/junkdog/artemis-odb) · last commit 2021
* [tiny-ecs](https://github.com/bakpakin/tiny-ecs) - Entity Component System for Lua that's simple, flexible, and useful. [⭐ 789](https://github.com/bakpakin/tiny-ecs) · last commit 2020
* [DefaultEcs](https://github.com/Doraku/DefaultEcs) - ECS for syntax and usage simplicity with maximum performance. [⭐ 765](https://github.com/Doraku/DefaultEcs) · last commit 2023
* [Kengine](https://github.com/phisko/kengine) - Game engine with an Entity-Component-System (ECS) architecture. [⭐ 618](https://github.com/phisko/kengine) · last commit 2023
* [ecst](https://github.com/vittorioromeo/ecst) - Experimental C++14 multithreaded compile-time entity-compnent-system library. [⭐ 490](https://github.com/vittorioromeo/ecst) · last commit 2018
* 💀 [ECS](https://github.com/redxdev/ECS) - C++ single-header entity component system library. [⭐ 481](https://github.com/redxdev/ECS) · last commit 2019
* 💀 [anax](https://github.com/miguelmartin75/anax) - Open source C++ entity system. [⭐ 460](https://github.com/miguelmartin75/anax) · last commit 2021
* [ECS Lua](https://github.com/nidorx/ecs-lua) - A fast and easy to use ECS engine for game development. [⭐ 234](https://github.com/nidorx/ecs-lua) · last commit 2021
* [EntityPlus](https://github.com/Yelnats321/EntityPlus) - C++14 entity component system. [⭐ 192](https://github.com/Yelnats321/EntityPlus) · last commit 2020
* [EntityFu](https://github.com/NatWeiss/EntityFu) - A simple, fast entity component system written in C++. [⭐ 86](https://github.com/NatWeiss/EntityFu) · last commit 2016
* [LeoEcsLite](https://github.com/LeoECSCommunity/ecslite) - Lightweight C# Entity Component System framework. [⭐ 62](https://github.com/LeoECSCommunity/ecslite) · last commit 2022
* [Ginseng](https://github.com/apples/ginseng) - An ESC library designed for use in games. [⭐ 56](https://github.com/apples/ginseng) · last commit 2021
* [Nata](https://github.com/tesselode/nata) - Entity management for Lua. [⭐ 51](https://github.com/tesselode/nata) · last commit 2020
* [ecs.hpp](https://github.com/BlackMATov/ecs.hpp) - A single header C++14 entity component system library. [⭐ 41](https://github.com/BlackMATov/ecs.hpp) · last commit 2023
* [beast](https://github.com/sjl/beast) - Basic Entity/Aspect/System Toolkit. [⭐ 30](https://github.com/sjl/beast) · last commit 2021
* [matter](https://github.com/frengels/matter) - C++17/20 ECS implementation. [⭐ 21](https://github.com/frengels/matter) · last commit 2019
* [Fast ECS](https://github.com/QiXi/fast_ecs) - Simple and fast Entity-Component-System (ECS) library written in Dart. [⭐ 17](https://github.com/QiXi/fast_ecs) · last commit 2021
* [goomy](https://github.com/vberlier/goomy) - A tiny, experimental ECS framework. [⭐ 14](https://github.com/vberlier/goomy) · last commit 2019
* [cl-ecs](https://github.com/bit-phlippers/cl-ecs) - An implementation of the Entity-Component-System pattern mostly used in game development. [⭐ 8](https://github.com/bit-phlippers/cl-ecs) · last commit 2016

</details>

## [Applications powered by ECS](#contents)

### [Game Engines](#contents)

_Game engines built on ECS architecture._

#### C++

* 🟢 [WickedEngine](https://github.com/turanszkij/WickedEngine) - 3D engine with modern graphics. [⭐ 7.3k](https://github.com/turanszkij/WickedEngine)
* 🟢 [halley](https://github.com/amzeratul/halley) - A lightweight game engine written in modern C++. [⭐ 3.9k](https://github.com/amzeratul/halley)
* 🟢 [Lumos](https://github.com/jmorton06/Lumos) - Cross-Platform C++ 2D/3D game engine. [⭐ 1.6k](https://github.com/jmorton06/Lumos)
* 🟡 [MxEngine](https://github.com/asc-community/MxEngine) - C++ open source 3D game engine. [⭐ 1.2k](https://github.com/asc-community/MxEngine)
* 🟢 [nebula](https://github.com/gscept/nebula) - Open-source and free-to-use modern C++ game engine. [⭐ 1.1k](https://github.com/gscept/nebula)
* 🟡 [Lina Engine](https://github.com/inanevin/LinaEngine) - Modular, tiny and fast C++ game engine, aimed to develop 3D desktop games. [⭐ 899](https://github.com/inanevin/LinaEngine)
* 🟢 [supernova](https://github.com/doriaxengine/doriax) - Game engine for 2D and 3D projects with ECS and data-oriented design. [⭐ 866](https://github.com/supernovaengine/supernova)
* 🟢 [Nazara Engine](https://github.com/NazaraEngine/NazaraEngine) - Cross-platform framework aimed at real-time applications requiring audio, 2D and 3D real-time rendering, network and more. [⭐ 843](https://github.com/NazaraEngine/NazaraEngine)
* 🟢 [crown](https://github.com/dbartolini/crown) - General purpose data-driven game engine. [⭐ 30](https://github.com/dbartolini/crown)

#### Go

* 🟡 [Engo](https://github.com/EngoEngine/engo) - A cross-platform game engine written in Go following an interpretation of the Entity Component System paradigm. [⭐ 1.8k](https://github.com/EngoEngine/engo)

#### Rust

* 🟢 [Bevy](https://github.com/bevyengine/bevy) - A refreshingly simple data-driven game engine built in Rust. [⭐ 48.9k](https://github.com/bevyengine/bevy)
* 🟡 [Ambient](https://github.com/AmbientRun/Ambient) - The multiplayer game engine. [⭐ 3.9k](https://github.com/AmbientRun/Ambient)
* 🟢 [Bones](https://github.com/fishfolk/bones) - An easy-to-use game engine for making real games. [⭐ 314](https://github.com/fishfolk/bones)

#### Zig

* 🟢 [mach](https://github.com/hexops/mach) - Game engine & graphics toolkit for building high-performance, truly cross-platform, robust & modular games, visualizations, and desktop/mobile GUI apps. [⭐ 4.8k](https://github.com/hexops/mach)

<details>
<summary>Inactive (7): archived or no commits for 3+ years</summary>

* 💀 [Amethyst](https://github.com/amethyst/amethyst) - Data-oriented and data-driven game engine written in Rust. [⭐ 8k](https://github.com/amethyst/amethyst) · last commit 2021
* [Sparky](https://github.com/TheCherno/Sparky) - Cross-Platform High Performance 2D/3D game engine. [⭐ 1.2k](https://github.com/TheCherno/Sparky) · last commit 2016
* [kengine](https://github.com/phisko/kengine) - Game engine focused on ease-of-use, runtime extensibility and compile-time type safety. [⭐ 618](https://github.com/phisko/kengine) · last commit 2023
* [Engine](https://github.com/Shervanator/Engine) - Basic cross-platform 3D game engine. [⭐ 301](https://github.com/Shervanator/Engine) · last commit 2018
* 💀 [shiva](https://github.com/Milerius/shiva) - Modern Cross-Platform C++ Engine with modularity. [⭐ 160](https://github.com/Milerius/shiva) · last commit 2019
* [Usagi](https://github.com/vitei/Usagi) - Hierarchical component entity system based game engine. [⭐ 57](https://github.com/vitei/Usagi) · last commit 2022
* [igneous](https://github.com/MissingBitStudios/igneous) - Open source game engine written in C++. [⭐ 52](https://github.com/MissingBitStudios/igneous) · last commit 2019

</details>

### [Graphics Engines](#contents)

_Graphics and rendering engines using ECS._

#### C++

* 🟢 [The Forge](https://github.com/ConfettiFX/The-Forge) - Cross-Platform Rendering Framework with support for PC Windows, Linux, Ray Tracing, macOS/iOS, Android, XBOX, PS4, PS5, Switch, Quest 2. [⭐ 5.7k](https://github.com/ConfettiFX/The-Forge)
* 🟢 [bs::framework](https://github.com/GameFoundry/B3DFramework) - Modern C++14 library for the development of real-time graphical applications. [⭐ 1.9k](https://github.com/GameFoundry/bsf)

### [Physics Libraries](#contents)

_Physics simulation libraries organized as ECS._

#### C++

* 🟢 [edyn](https://github.com/xissburg/edyn) - A real-time physics engine organized as an ECS. [⭐ 792](https://github.com/xissburg/edyn)

## [Other Resources](#contents)

### [Benchmarks](#contents)

_Performance benchmarks comparing ECS frameworks._

* 🟡 [ecs_benchmark](https://github.com/abeimler/ecs_benchmark) - Benchmarks of common ECS (Entity-Component-System)-Frameworks in C/C++. [⭐ 308](https://github.com/abeimler/ecs_benchmark)
* 🟢 [ECS C# Benchmark](https://github.com/Doraku/Ecs.CSharp.Benchmark) - Benchmarks of the main ECS Frameworks for: C#. [⭐ 181](https://github.com/Doraku/Ecs.CSharp.Benchmark)
* 🟢 [ECS C# Benchmark - Common uses-cases](https://github.com/friflo/ECS.CSharp.Benchmark-common-use-cases) - Benchmark many common use cases in the simplest and most performant variant. [⭐ 48](https://github.com/friflo/ECS.CSharp.Benchmark-common-use-cases)
* [CSharpECSComparison](https://github.com/Chillu1/CSharpECSComparison) - Benchmarks of common ECS Frameworks for C#. [⭐ 53](https://github.com/Chillu1/CSharpECSComparison)
* 🟢 [Lua ECS Library Benchmark](https://github.com/jeffzi/lua-ecs-benchmark) - Benchmarks of common ECS Frameworks in Lua. [⭐ 9](https://github.com/jeffzi/lua-ecs-benchmark)

### [Blog Posts](#contents)

_Articles and blog posts about ECS and data-oriented design._

* [Data-oriented design](https://gamesfromwithin.com/category/data-oriented-design/)
* [ECS back and forth](https://skypjack.github.io/2019-02-14-ecs-baf-part-1/)
* [Let's build an Entity Component System from scratch](https://devlog.hexops.com/2022/lets-build-ecs-part-1/)
* [Entity Systems are the future of MMOG development](https://t-machine.org/index.php/2007/09/03/entity-systems-are-the-future-of-mmog-development-part-1/)
* [Building an ECS](https://ajmmertens.medium.com/building-an-ecs-1-where-are-my-entities-and-components-63d07c7da742)
* [Systems Interaction in Entity-Component-System (events)](https://medium.com/@ben.rasooli/systems-interaction-in-entity-component-system-events-4a050153c8ac)
* [Overview of ECS variants & definitions](https://gist.github.com/LearnCocos2D/77f0ced228292676689f)
* [Understand data-oriented design](https://learn.unity.com/tutorial/part-1-understand-data-oriented-design)
* [Unity ECS series](https://gametorrahod.com/tag/unity-dots/)
* [Seba's Lab](https://www.sebaslab.com/)
* [WickedEngine's ECS implementation](https://web.archive.org/web/20240531144559/https://wickedengine.net/2019/09/entity-component-system/)

### [Talks & Slides](#contents)

_Conference talks and presentations about ECS._

* [itCppCon19: ECS back and forth](https://youtu.be/WB5bRKKGRUk)
* [GDC 2018: Unity at GDC - A Data Oriented Approach to Using Component Systems](https://youtu.be/p65Yt20pw0g)
* [Meeting C++ 2018: Data oriented design in practice](https://youtu.be/NWMx1Q66c14)
* [CppCon 2018: Stoyan Nikolov “OOP Is Dead, Long Live Data-oriented Design”](https://youtu.be/yy8jQgmhbAU)
* [Data Oriented Design Resources](http://web.archive.org/web/20260930161104/https://aras-p.info/texts/files/2018Academy%20-%20ECS-DoD.pdf)
* [Data Oriented GUI in Rust](https://www.youtube.com/watch?v=4YTfxresvS8)
* [Is There More to Game Architecture than ECS](https://www.youtube.com/watch?v=JxI3Eu5DPwE) - Bob Nystrom (Roguelike Celebration 2018)
* [Unite 2018: C# Job System + ECS usage and demo with Intel](https://www.youtube.com/watch?v=fp1D45hhVEM)
* [Codestar 2018 ECS - A Different Approach to Game Development](https://www.youtube.com/watch?v=lt4eL4RSx7k)
* [CppCon 2014: Mike Acton "Data-Oriented Design and C++"](https://youtu.be/rX0ItVEVjHc)

### [Books](#contents)

_Books on ECS and data-oriented design._

* [Data-Oriented Design](https://www.dataorienteddesign.com/dodbook/)

### [Tutorials](#contents)

_Tutorial series for learning ECS._

* [Starting a new 2D platformer with ECS](https://www.youtube.com/playlist?list=PLWtPciJ1UMuAoCq8NAw8J-n387U4QHFBW)

### [Lists](#contents)

_Related curated lists._

* [Entity Component System & Data Oriented Design](https://github.com/dbartolini/data-oriented-design)

### [References](#contents)

_Wikis, FAQs, glossaries, and other reference material on ECS._

* [Entity Systems Wiki](http://entity-systems.wikidot.com/)
* [Entity Component Systems FAQ](https://github.com/SanderMertens/ecs-faq)

## [Contributing](#contents)

Contributions are very welcome! Please read the [contribution guidelines](https://github.com/jslee02/awesome-entity-component-system/blob/main/CONTRIBUTING.md) first. Also, please feel free to report any error.

## [Star History](#contents)

<a href="https://www.star-history.com/?repos=jslee02%2Fawesome-entity-component-system">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=jslee02/awesome-entity-component-system&type=date&theme=dark&legend=top-left" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=jslee02/awesome-entity-component-system&type=date&legend=top-left" />
    <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=jslee02/awesome-entity-component-system&type=date&legend=top-left" />
  </picture>
</a>

## [License](#contents)

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)
