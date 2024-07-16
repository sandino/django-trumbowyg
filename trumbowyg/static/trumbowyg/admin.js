document.addEventListener("DOMContentLoaded", () => {
  if (document.body.getAttribute("data-admin-utc-offset") !== null) {
    if (window.matchMedia("(prefers-color-scheme: dark)").matches) {
      document.documentElement.classList.add("trumbowyg-dark");
    }

    const documentElementObserver = new MutationObserver((records) => {
      for (const record of records) {
        if (record.attributeName === "data-theme") {
          const theme = document.documentElement.getAttribute("data-theme");

          if (theme === "auto") {
            if (window.matchMedia("(prefers-color-scheme: dark)").matches) {
              document.documentElement.classList.add("trumbowyg-dark");
            } else {
              document.documentElement.classList.remove("trumbowyg-dark");
            }
          } else if (theme === "light") {
            document.documentElement.classList.remove("trumbowyg-dark");
          } else {
            document.documentElement.classList.add("trumbowyg-dark");
          }
        }
      }
    });

    documentElementObserver.observe(document.documentElement, {
      attributes: true,
    });
  }
});
