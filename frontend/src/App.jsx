import { useEffect, useMemo, useState } from "react";
import "./styles.css";

const API_BASE = import.meta.env.VITE_API_BASE || "/api";

const fallbackContent = {
  profile: {
    brand_name: "Iqra Yeafhy Ira",
    logo: "",
    tagline: "Content Designer and Social Media Manager | CSE Graduate",
    hero_badge: "Content Designer and Social Media Manager",
    hero_title:
      "Hi, I am Iqra Yeafhy Ira. I design social media content and brand visuals with a soft, modern style.",
    hero_subtitle:
      "Creative and detail-oriented Social Media Manager and Content Designer with experience delivering high-volume, high-quality visuals for international clients.",
    hero_card_title: "Social and Visual Design",
    hero_card_body: "Canva, CapCut, Meta Suite, and content planning",
    availability: "Open to new projects",
    location: "Uttara, Dhaka",
    email: "iqrayeafhy@gmail.com",
    phone: "+880 151800000",
    cta_primary_text: "View my work",
    cta_primary_target: "#work",
    cta_secondary_text: "My skills",
    cta_secondary_target: "#skills",
    footer_text: "Designing with clarity, consistency, and care.",
    header_cta_text: "Lets chat",
    header_cta_target: "#contact",
    favicon_url: "",
    about_intro:
      "Creative and detail-oriented Social Media Manager and Content Designer. Skilled in Canva, CapCut, and cross-platform scheduling. Currently finishing a B.Sc. in Computer Science and Engineering with research in AI-assisted patient referral systems.",
    services_intro:
      "Social media design, content planning, brand visuals, and scheduling for growing businesses.",
  skills_intro:
      "Design tools, social strategy, and production workflows used to deliver fast, consistent content.",
    work_intro:
      "A mix of social media designs, marketing visuals, and brand content.",
    experience_intro:
      "Experience across agencies and remote teams delivering content at scale.",
    contact_intro:
      "Reach out for social media design, content calendars, and branding visuals.",
    features_intro:
      "Reliable delivery, consistent brand style, and hands-on social publishing.",
  },
  aboutCards: [
    {
      id: 1,
      title: "B.Sc. in Computer Science and Engineering",
      body:
        "World University of Bangladesh. CGPA 3.64 / 4.00 (final semester, 138/148 credits).",
      order: 0,
      is_active: true,
    },
    {
      id: 2,
      title: "Higher Secondary Certificate (HSC)",
      body:
        "Uttara High School and College. Result 4.25 / 5.00.",
      order: 1,
      is_active: true,
    },
    {
      id: 3,
      title: "Secondary School Certificate (SSC)",
      body:
        "Uttara High School and College. Result 4.06 / 5.00.",
      order: 2,
      is_active: true,
    },
  ],
  services: [
    {
      id: 1,
      title: "Social Media Strategy and Scheduling",
      body:
        "Plan, design, and schedule content that matches brand tone and platform goals.",
      order: 0,
      is_active: true,
    },
    {
      id: 2,
      title: "Canva and Visual Design",
      body:
        "Carousel posts, banners, and marketing visuals with consistent brand style.",
      order: 1,
      is_active: true,
    },
    {
      id: 3,
      title: "CapCut Video Editing",
      body:
        "Short-form reels, edits, and pacing optimized for engagement.",
      order: 2,
      is_active: true,
    },
    {
      id: 4,
      title: "Content Calendar Planning",
      body:
        "Weekly and monthly content planning with templates and workflow support.",
      order: 3,
      is_active: true,
    },
  ],
  highlights: [
    { id: 1, label: "Visual assets delivered in 1 month", value: "147", order: 0, is_active: true },
    { id: 2, label: "Hours worked in one month", value: "110+", order: 1, is_active: true },
    { id: 3, label: "Extra hours to meet deadlines", value: "20+", order: 2, is_active: true },
    { id: 4, label: "CGPA", value: "3.64", order: 3, is_active: true },
  ],
  socials: [
    { id: 1, label: "LinkedIn", url: "https://linkedin.com/in/iqrayeafhyira/", icon: "", order: 0 },
  ],
  projects: [
    {
      id: 1,
      title: "International Client Social Pack",
      description:
        "High-volume social kit with posts, reels, graphics, and banners.",
      category: "Social Design",
      url: "https://behance.net",
      image: "",
    },
    {
      id: 2,
      title: "Brand Visual Refresh",
      description:
        "Modern templates and visuals aligned to brand tone and consistency.",
      category: "Branding",
      url: "https://behance.net",
      image: "",
    },
    {
      id: 3,
      title: "Marketing Visual Series",
      description:
        "Promotional posts and visuals for campaigns and offers.",
      category: "Marketing",
      url: "https://behance.net",
      image: "",
    },
    {
      id: 4,
      title: "Event Posters and Banners",
      description:
        "Posters and event visuals created for university programs.",
      category: "Print",
      url: "https://behance.net",
      image: "",
    },
  ],
  skills: [
    { id: 1, name: "Social Media Strategy and Scheduling", proficiency: "Advanced" },
    { id: 2, name: "Canva and Visual Design", proficiency: "Advanced" },
    { id: 3, name: "CapCut Video Editing", proficiency: "Advanced" },
    { id: 4, name: "Meta Business Suite", proficiency: "Intermediate" },
    { id: 5, name: "AI Assisted Content Workflow", proficiency: "Intermediate" },
    { id: 6, name: "Content Calendar Planning", proficiency: "Advanced" },
    { id: 7, name: "MS and Google Office Suite", proficiency: "Intermediate" },
  ],
  experiences: [
    {
      id: 1,
      job_title: "Social Media and Content Manager (Promoted)",
      company: "Call The Cleaners, Australia - Remote",
      start_date: "2025-08-01",
      end_date: "",
      description:
        "Promoted from part-time designer to full-time Social Media Manager. Responsible for designing, scheduling, and publishing posts and reels with publishing rights on Meta.",
    },
    {
      id: 2,
      job_title: "Social Media Content Creator and Designer",
      company: "ElitSpire, Australia - Remote",
      start_date: "2024-01-01",
      end_date: "2025-08-01",
      description:
        "Designed posts and reels, created marketing visuals, and scheduled content across social platforms.",
    },
    {
      id: 3,
      job_title: "Social Media and Creative Designer",
      company: "360 Photo Booth BD",
      start_date: "2023-01-01",
      end_date: "2024-01-01",
      description:
        "Transformed older content themes into new designs, reels, and static posts aligned with brand tone.",
    },
    {
      id: 4,
      job_title: "Social Media Assistant",
      company: "TiqBud - Dhaka, Bangladesh",
      start_date: "2022-08-01",
      end_date: "2023-01-01",
      description:
        "Managed creative production and ensured engaging content. Increased organic reach via reels and Canva graphics.",
    },
    {
      id: 5,
      job_title: "Graphics Designer (Volunteer)",
      company: "WUBCS",
      start_date: "2022-01-01",
      end_date: "2023-01-01",
      description:
        "Designed posters, banners, and event visuals for university tech events and promotions.",
    },
  ],
  features: [
    {
      id: 1,
      title: "High-volume delivery",
      body:
        "Delivered 147 assets in a single month across posts, reels, and graphics.",
      order: 0,
      is_active: true,
    },
    {
      id: 2,
      title: "Reliable scheduling",
      body:
        "Publishing rights on Meta and cross-platform scheduling experience.",
      order: 1,
      is_active: true,
    },
    {
      id: 3,
      title: "Content consistency",
      body:
        "Brand-aligned visuals with strong storytelling and consistent tone.",
      order: 2,
      is_active: true,
    },
    {
      id: 4,
      title: "AI-assisted workflows",
      body:
        "Used AI tools to plan and streamline content workflows.",
      order: 3,
      is_active: true,
    },
  ],
  process: [],
};

const unwrap = (payload) =>
  Array.isArray(payload) ? payload : payload?.results ?? [];

const formatDate = (value) => {
  if (!value) return "Present";
  const parsed = new Date(value);
  if (Number.isNaN(parsed.getTime())) return value;
  return parsed.toLocaleDateString("en-US", { month: "short", year: "numeric" });
};

const skillToPercent = (value) => {
  if (!value) return 50;
  const numeric = Number(value);
  if (!Number.isNaN(numeric)) return Math.max(20, Math.min(numeric, 100));
  const map = {
    beginner: 40,
    intermediate: 65,
    advanced: 85,
    expert: 95,
  };
  return map[value.toLowerCase()] ?? 55;
};

const resolveImage = (value) => {
  if (!value) return "";
  if (value.startsWith("http")) return value;
  if (value.startsWith("/")) return value;
  return `/media/${value}`;
};

const filterActive = (items) =>
  items.filter((item) => item.is_active !== false);

export default function App() {
  const [content, setContent] = useState(fallbackContent);
  const [source, setSource] = useState("loading");
  const [selectedCategory, setSelectedCategory] = useState("All");
  const [theme, setTheme] = useState("light");

  useEffect(() => {
    let active = true;

    const load = async () => {
      const endpoints = [
        "projects",
        "skills",
        "experiences",
        "profile",
        "about-cards",
        "services",
        "highlights",
        "socials",
        "features",
      ];

      const results = await Promise.allSettled(
        endpoints.map((endpoint) => fetch(`${API_BASE}/${endpoint}/`))
      );

      const next = { ...fallbackContent };

      const resolved = await Promise.all(
        results.map(async (result) => {
          if (result.status !== "fulfilled" || !result.value.ok) {
            return null;
          }
          return result.value.json();
        })
      );

      const dataMap = Object.fromEntries(
        endpoints.map((endpoint, index) => [endpoint, resolved[index]])
      );

      if (dataMap.projects) next.projects = unwrap(dataMap.projects);
      if (dataMap.skills) next.skills = unwrap(dataMap.skills);
      if (dataMap.experiences) next.experiences = unwrap(dataMap.experiences);

      if (dataMap.profile) {
        const profileList = unwrap(dataMap.profile);
        if (profileList.length > 0) {
          next.profile = { ...next.profile, ...profileList[0] };
        }
      }

      if (dataMap["about-cards"]) {
        next.aboutCards = filterActive(unwrap(dataMap["about-cards"]));
      }
      if (dataMap.services) {
        next.services = filterActive(unwrap(dataMap.services));
      }
      if (dataMap.highlights) {
        next.highlights = filterActive(unwrap(dataMap.highlights));
      }
      if (dataMap.socials) {
        next.socials = filterActive(unwrap(dataMap.socials));
      }
      if (dataMap.features) {
        next.features = filterActive(unwrap(dataMap.features));
      }

      if (!active) return;
      setContent(next);
      setSource(
        results.every((result) => result.status === "fulfilled" && result.value.ok)
          ? "api"
          : "fallback"
      );
    };

    load();
    return () => {
      active = false;
    };
  }, []);

  useEffect(() => {
    if (content.profile?.seo_title) {
      document.title = content.profile.seo_title;
    }
    const meta = document.querySelector('meta[name="description"]');
    if (meta && content.profile?.seo_description) {
      meta.setAttribute("content", content.profile.seo_description);
    }

    if (content.profile?.favicon_url || content.profile?.favicon) {
      const href = content.profile?.favicon_url
        ? content.profile.favicon_url
        : resolveImage(content.profile.favicon);
      let link = document.querySelector("link[rel='icon']");
      if (!link) {
        link = document.createElement("link");
        link.rel = "icon";
        document.head.appendChild(link);
      }
      link.href = href;
    }
  }, [content.profile]);

  useEffect(() => {
    const saved = window.localStorage.getItem("theme");
    const preferred = saved || "light";
    setTheme(preferred);
    document.documentElement.setAttribute("data-theme", preferred);
  }, []);

  const toggleTheme = () => {
    const next = theme === "dark" ? "light" : "dark";
    setTheme(next);
    window.localStorage.setItem("theme", next);
    document.documentElement.setAttribute("data-theme", next);
  };


  const categories = useMemo(() => {
    const names = content.projects
      .map((project) => project.category)
      .filter(Boolean);
    return ["All", ...new Set(names)];
  }, [content.projects]);

  const filteredProjects = useMemo(() => {
    if (selectedCategory === "All") return content.projects;
    return content.projects.filter(
      (project) => project.category === selectedCategory
    );
  }, [content.projects, selectedCategory]);

  useEffect(() => {
    if (!categories.includes(selectedCategory)) {
      setSelectedCategory("All");
    }
  }, [categories, selectedCategory]);

  const handleMail = (event) => {
    event.preventDefault();
    const form = new FormData(event.target);
    const name = form.get("name");
    const message = form.get("message");
    const subject = encodeURIComponent(`Portfolio hello from ${name}`);
    const body = encodeURIComponent(message);
    const email = content.profile?.email || "hello@yourname.com";
    window.location.href = `mailto:${email}?subject=${subject}&body=${body}`;
  };

  const brandInitial = content.profile?.brand_name
    ? content.profile.brand_name[0]
    : "B";

  const heroBadge = content.profile?.hero_badge || content.profile?.tagline;

  const platformFromUrl = (url, fallback) => {
    if (!url) return fallback || "Social";
    try {
      const host = new URL(url).hostname.replace("www.", "");
      const map = {
        "linkedin.com": "LinkedIn",
        "instagram.com": "Instagram",
        "facebook.com": "Facebook",
        "behance.net": "Behance",
        "dribbble.com": "Dribbble",
        "youtube.com": "YouTube",
        "tiktok.com": "TikTok",
        "github.com": "GitHub",
      };
      for (const key of Object.keys(map)) {
        if (host.includes(key)) return map[key];
      }
      return fallback || host;
    } catch (error) {
      return fallback || "Social";
    }
  };

  const linkedInLink = content.socials.find((item) =>
    platformFromUrl(item.url, item.label).toLowerCase().includes("linkedin")
  );

  return (
    <div>
      <header className="site-header">
        <div className="container nav">
          <a className="brand" href="/">
            {content.profile?.logo ? (
              <img
                src={resolveImage(content.profile.logo)}
                alt={content.profile?.brand_name}
                className="brand-logo"
              />
            ) : (
              <span className="brand-mark">{brandInitial}</span>
            )}
            <span>{content.profile?.brand_name}</span>
          </a>
          <nav className="nav-links">
            <a href="#home">Home</a>
            <a href="#about">Education</a>
            <a href="#features">Features</a>
            <a href="#services">Services</a>
            <a href="#skills">Skills</a>
            <a href="#work">Work</a>
            <a href="#experience">Experience</a>
          </nav>
          <div className="nav-actions">
            <a
              className="btn btn-primary nav-cta"
              href={content.profile?.header_cta_target || "#contact"}
            >
              {content.profile?.header_cta_text || "Lets chat"}
            </a>
            <button
              className="emoji-toggle"
              onClick={toggleTheme}
              type="button"
              aria-label="Toggle theme"
            >
              {theme === "dark" ? "☀️" : "🌙"}
            </button>
          </div>
        </div>
      </header>

      <main>
        <section id="home" className="container hero">
          <div className="reveal" style={{ "--delay": "0s" }}>
            {heroBadge && <span className="pill">{heroBadge}</span>}
            <h1>{content.profile?.hero_title}</h1>
            <p>{content.profile?.hero_subtitle}</p>
            <div className="hero-actions">
              <a className="btn btn-primary" href={content.profile?.cta_primary_target}>
                {content.profile?.cta_primary_text}
              </a>
              <a
                className="btn btn-secondary"
                href={content.profile?.cta_secondary_target}
              >
                {content.profile?.cta_secondary_text}
              </a>
              {linkedInLink && (
                <a
                  className="btn btn-secondary"
                  href={linkedInLink.url}
                  target="_blank"
                  rel="noreferrer"
                >
                  LinkedIn
                </a>
              )}
            </div>
            <div className="stats">
              {content.highlights.map((item, index) => (
                <div
                  className="stat-card reveal"
                  key={item.id ?? item.label}
                  style={{ "--delay": `${0.2 + index * 0.1}s` }}
                >
                  <h4>{item.value}</h4>
                  <p>{item.label}</p>
                </div>
              ))}
            </div>
          </div>

          <div className="hero-card reveal" style={{ "--delay": "0.1s" }}>
            <div className="portrait">
              {content.profile?.hero_image ? (
                <img
                  src={resolveImage(content.profile.hero_image)}
                  alt={content.profile?.brand_name}
                  className="portrait-image"
                />
              ) : (
                <div className="portrait-inner">
                  {content.profile?.availability && (
                    <span className="badge">{content.profile.availability}</span>
                  )}
                  <h3>{content.profile?.hero_card_title}</h3>
                  <p>{content.profile?.hero_card_body}</p>
                </div>
              )}
            </div>
          </div>
        </section>

        <section id="about">
          <div className="container">
            <h2 className="section-title">Education</h2>
            <p className="section-subtitle">
              {content.profile?.about_intro ||
                "Academic background and research focus."}
            </p>
            <div className="grid-3">
              {content.aboutCards.map((card, index) => (
                <div
                  className="card reveal"
                  key={card.id ?? card.title}
                  style={{ "--delay": `${index * 0.1}s` }}
                >
                  <h3>{card.title}</h3>
                  <p>{card.body}</p>
                </div>
              ))}
            </div>
          </div>
        </section>

        <section id="features">
          <div className="container">
            <h2 className="section-title">Featured strengths</h2>
            <p className="section-subtitle">
              {content.profile?.features_intro ||
                "Soft, consistent visuals with a thoughtful process behind every post."}
            </p>
            <div className="grid-3">
              {content.features.map((feature, index) => (
                <div
                  className="card reveal"
                  key={feature.id ?? feature.title}
                  style={{ "--delay": `${index * 0.1}s` }}
                >
                  <h3>{feature.title}</h3>
                  <p>{feature.body}</p>
                </div>
              ))}
            </div>
          </div>
        </section>

        <section id="services">
          <div className="container">
            <h2 className="section-title">Services I love</h2>
            <p className="section-subtitle">
              {content.profile?.services_intro ||
                "Cute, brand-safe visuals for social media plus beginner-friendly UI/UX exploration."}
            </p>
            <div className="grid-3">
              {content.services.map((service, index) => (
                <div
                  className="card reveal"
                  key={service.id ?? service.title}
                  style={{ "--delay": `${index * 0.1}s` }}
                >
                  <h3>{service.title}</h3>
                  <p>{service.body}</p>
                </div>
              ))}
            </div>
          </div>
        </section>


        <section id="skills">
          <div className="container">
            <h2 className="section-title">Skill stack</h2>
            <p className="section-subtitle">
              {content.profile?.skills_intro ||
                "Blending visual design tools with new UI/UX skills as I grow."}
            </p>
            <div className="skills-grid">
              {content.skills.map((skill, index) => (
                <div
                  className="skill reveal"
                  key={skill.id ?? skill.name}
                  style={{ "--delay": `${index * 0.08}s` }}
                >
                  <strong>{skill.name}</strong>
                  <div className="skill-bar">
                    <span
                      style={{
                        width: `${skillToPercent(skill.proficiency)}%`,
                      }}
                    />
                  </div>
                  <small>{skill.proficiency}</small>
                </div>
              ))}
            </div>
          </div>
        </section>

        <section id="work">
          <div className="container">
            <h2 className="section-title">Selected work</h2>
            <p className="section-subtitle">
              {content.profile?.work_intro ||
                "A mix of social media designs, brand visuals, and early UI/UX concepts."}
            </p>
            {source === "fallback" && (
              <p className="pill" style={{ marginTop: "1rem" }}>
                Showing sample projects. Add your own in the dashboard.
              </p>
            )}
            <div className="projects">
              <div className="filter-row">
                {categories.map((category) => (
                  <button
                    key={category}
                    className={`chip ${
                      selectedCategory === category ? "active" : ""
                    }`}
                    onClick={() => setSelectedCategory(category)}
                    type="button"
                  >
                    {category}
                  </button>
                ))}
              </div>
              <div className="project-grid">
                {filteredProjects.length === 0 ? (
                  <div className="card">
                    <h3>No projects yet</h3>
                    <p>
                      Add projects in the dashboard to make this section shine.
                    </p>
                  </div>
                ) : (
                  filteredProjects.map((project, index) => (
                    <article
                      className="project-card reveal"
                      key={project.id ?? project.title}
                      style={{ "--delay": `${index * 0.08}s` }}
                    >
                      <div className="project-image">
                        {project.image ? (
                          <img
                            src={resolveImage(project.image)}
                            alt={project.title}
                            loading="lazy"
                          />
                        ) : (
                          <span>Soft visuals coming soon</span>
                        )}
                      </div>
                      <div className="project-body">
                        {project.category && (
                          <span className="tag">{project.category}</span>
                        )}
                        <h3>{project.title}</h3>
                        <p>{project.description}</p>
                        {project.url && (
                          <a
                            className="btn btn-secondary"
                            href={project.url}
                            target="_blank"
                            rel="noreferrer"
                          >
                            View project
                          </a>
                        )}
                      </div>
                    </article>
                  ))
                )}
              </div>
            </div>
          </div>
        </section>

        <section id="experience">
          <div className="container">
            <h2 className="section-title">Experience</h2>
            <p className="section-subtitle">
              {content.profile?.experience_intro ||
                "Real-world social design work, client projects, and growing responsibilities."}
            </p>
            <div className="timeline">
              {content.experiences.map((item, index) => (
                <div
                  className="timeline-item reveal"
                  key={item.id ?? item.job_title}
                  style={{ "--delay": `${index * 0.1}s` }}
                >
                  <h3>
                    {item.job_title} - {item.company}
                  </h3>
                  <p>
                    {formatDate(item.start_date)} - {formatDate(item.end_date)}
                  </p>
                  <p>{item.description}</p>
                </div>
              ))}
            </div>
          </div>
        </section>

        <section id="contact">
          <div className="container">
            <h2 className="section-title">Lets create together</h2>
            <p className="section-subtitle">
              {content.profile?.contact_intro ||
                "Tell me about your brand or project. I would love to make something sweet, clear, and memorable."}
            </p>
            <div className="contact-grid">
              <div className="contact-card reveal" style={{ "--delay": "0s" }}>
                <h3>Contact details</h3>
                {content.profile?.email && <p>Email: {content.profile.email}</p>}
                {content.profile?.phone && <p>Phone: {content.profile.phone}</p>}
                {content.profile?.location && (
                  <p>Location: {content.profile.location}</p>
                )}
                <div className="grid-3" style={{ marginTop: "1rem" }}>
                  {content.socials.map((item) => (
                    <a
                      key={item.id ?? item.label}
                      className="chip social-chip"
                      href={item.url}
                      target="_blank"
                      rel="noreferrer"
                    >
                      {platformFromUrl(item.url, item.label)}
                    </a>
                  ))}
                </div>
              </div>
              <div className="contact-card reveal" style={{ "--delay": "0.1s" }}>
                <h3>Quick hello</h3>
                <form onSubmit={handleMail}>
                  <input name="name" placeholder="Your name" required />
                  <textarea
                    name="message"
                    placeholder="What do you want to create?"
                    required
                  />
                  <button className="btn btn-primary" type="submit">
                    Send a message
                  </button>
                </form>
              </div>
            </div>
          </div>
        </section>
      </main>

      <footer className="footer">
        <div className="container">
          <p>{content.profile?.footer_text}</p>
        </div>
      </footer>
    </div>
  );
}
