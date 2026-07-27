# AGENTS.md

# Alt+Tab Soundtrack - AI Development Instructions

## Purpose

This document defines how AI agents should contribute to this repository.

The goal is to preserve the existing architecture, coding style, and development philosophy. New code should integrate naturally with the current project instead of introducing different patterns or unnecessary abstractions.

---

# General Principles

Always prioritize:

- Readability
- Simplicity
- Maintainability
- Consistency
- Reusability

Never optimize code at the cost of readability.

The project should feel like it was written by a single developer.

---

# Project Philosophy

This project favors practical, maintainable solutions over enterprise design patterns.

When contributing:

- Prefer extending existing code instead of introducing new abstractions.
- Keep the architecture simple and easy to understand.
- Avoid creating layers that provide little or no benefit.
- Favor explicit code over "magic" solutions.
- Write code that another developer can understand quickly.

Avoid introducing:

- Dependency Injection frameworks
- Repository patterns for simple CRUD operations
- Factory patterns without a clear need
- Excessive interfaces or abstract classes
- Over-engineered architectures
- Premature optimization

Small, focused classes are preferred over large, highly abstract systems.

The project should remain lightweight, pragmatic, and easy to maintain.

# Preserve Existing Style

When editing existing files:

- Match the surrounding coding style.
- Preserve naming conventions.
- Preserve the existing architecture.
- Do not rewrite code only to match personal preferences.
- Minimize the size of changes.

A small, consistent change is preferred over a large refactor.

# Before Writing Code

Before implementing anything:

- Read the surrounding code.
- Follow the existing architecture.
- Reuse existing classes whenever possible.
- Prefer extending existing modules instead of creating parallel implementations.
- Search the repository before creating new helpers or utilities.

Do not rewrite working code unless explicitly requested.

---

# Project Architecture

The project is organized by responsibility.

```
src/
│
├── assets/
├── configs/
├── cores/
├── data/
├── templates/
├── types/
├── ui/
└── utils/
```

Never change this structure without a strong reason.

---

# Folder Responsibilities

## configs/

Application configuration.

Examples:

- database
- playwright
- environment
- logging

No business logic belongs here.

---

## cores/

Contains the application's business logic.

Examples:

- Spotify
- LinkedIn
- HTML generation
- Database access
- Automation

This is the heart of the application.

---

## ui/

Contains only the graphical interface.

The UI should only:

- collect user input
- perform simple validation
- call async methods
- update widgets

Business logic must never be implemented inside the UI.

---

## utils/

Reusable helper functions.

Examples:

- exceptions
- enums
- helpers
- global utilities

---

## templates/

Contains HTML templates.

Python should only inject data into the template.

Do not generate HTML using string concatenation.

---

## assets/

Static files only.

Examples:

- CSS
- JavaScript
- Fonts
- Images

---

## data/

Persistent application data.

Examples:

- SQLite database
- Generated images
- Logs

---

# Coding Style

Follow the existing coding style.

Do not introduce different naming conventions.

Prefer explicit code over clever code.

Readable code is more important than shorter code.

---

# Type Hints

Every new function must be fully typed.

Use:

- Self
- Path
- Optional
- TypedDict
- Enum

when appropriate.

Never remove existing type hints.

---

# Naming

Classes:

```
PascalCase
```

Methods:

```
snake_case
```

Variables:

```
snake_case
```

Constants:

```
UPPER_CASE
```

---

# Async

This project is async-first.

Operations involving:

- Playwright
- SQLite
- HTTP requests
- File generation

should remain asynchronous.

Never replace async code with synchronous implementations.

Never block the Tkinter UI thread.

---

# UI Rules

The UI is responsible only for:

- reading user input
- updating widgets
- displaying messages
- triggering async operations

Heavy processing belongs in the Core layer.

---

# Playwright

Website automation should remain isolated.

Reuse the existing Site base class.

Prefer semantic locators over XPath.

Avoid duplicated selectors.

Reuse browser contexts whenever possible.

---

# Database

Keep database access centralized.

Never execute SQL directly inside UI classes.

Prefer reusable methods over duplicated queries.

---

# HTML Generation

The HTML template is the source of truth.

Do not recreate HTML inside Python.

Python should only inject values.

CSS should define presentation.

JavaScript should only support the HTML page.

---

# Error Handling

Never use:

```python
except:
```

Always use:

```python
except Exception as e:
```

Create custom exceptions whenever appropriate.

Do not silently ignore errors.

---

# Logging

Important operations should produce logs.

Examples:

- startup
- shutdown
- publishing
- errors
- database operations

---

# File Organization

Each file should have a single responsibility.

Avoid large files.

When a file grows significantly, split it into smaller modules.

---

# Paths

Always use:

```python
Path
```

or project helper functions.

Never hardcode absolute paths.

---

# Imports

Follow Python import conventions:

1. Standard library
2. Third-party packages
3. Internal modules

Import only what is necessary.

---

# Reuse

Before creating:

- a helper
- a utility
- a class
- a service

search the repository.

Avoid duplicated code.

---

# Dependencies

Prefer the Python standard library.

Only introduce new dependencies when they provide significant value.

Avoid unnecessary frameworks.

---

# Refactoring

Do not refactor unrelated code.

Do not rewrite files simply because another implementation would be cleaner.

Only refactor when:

- fixing bugs
- improving maintainability
- explicitly requested

Consistency is more important than perfection.

---

# Existing Patterns

Preserve the existing patterns used throughout the repository.

Examples include:

- async architecture
- Self type hints
- TypedDict models
- Enum usage
- Site inheritance
- centralized configuration
- helper utilities

Follow the surrounding code before introducing a new pattern.

---

# Code Generation

When implementing a new feature:

1. Reuse existing code.
2. Keep changes minimal.
3. Preserve public APIs whenever possible.
4. Follow the existing project structure.
5. Avoid introducing unnecessary abstractions.

---

# What to Avoid

Do not:

- duplicate code
- create giant classes
- create giant methods
- block the UI thread
- mix UI and business logic
- hardcode paths
- add unnecessary dependencies
- introduce inconsistent naming
- create parallel architectures
- rewrite working code without request

---

# Decision Priority

When multiple implementations are possible, prefer the one that:

1. Matches the existing project style.
2. Requires fewer changes.
3. Is easier to understand.
4. Is easier to maintain.

Consistency is always preferred over novelty.

---

# Final Goal

Every contribution should make the repository feel cohesive.

A developer reading the code should not be able to distinguish between manually written code and AI-generated code.