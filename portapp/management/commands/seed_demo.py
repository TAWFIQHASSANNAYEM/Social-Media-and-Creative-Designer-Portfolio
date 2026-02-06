from django.core.management.base import BaseCommand

from portapp.models import (
    AboutCard,
    Experience,
    Feature,
    Highlight,
    Project,
    Service,
    SiteProfile,
    Skill,
    SocialLink,
)


class Command(BaseCommand):
    help = "Seed demo data for the portfolio site."

    def handle(self, *args, **options):
        profile, created = SiteProfile.objects.get_or_create(
            pk=1,
            defaults={
                "brand_name": "Iqra Yeafhy Ira",
                "tagline": "Content Designer and Social Media Manager | CSE Graduate",
                "hero_badge": "Content Designer and Social Media Manager",
                "hero_title": "Hi, I am Iqra Yeafhy Ira. I design social media content and brand visuals with a soft, modern style.",
                "hero_subtitle": "Creative and detail-oriented Social Media Manager and Content Designer with experience delivering high-volume, high-quality visuals for international clients.",
                "hero_card_title": "Social and Visual Design",
                "hero_card_body": "Canva, CapCut, Meta Suite, and content planning",
                "availability": "Open to new projects",
                "location": "Uttara, Dhaka",
                "email": "iqrayeafhy@gmail.com",
                "phone": "+880 151800000",
                "cta_primary_text": "View my work",
                "cta_primary_target": "#work",
                "cta_secondary_text": "My skills",
                "cta_secondary_target": "#skills",
                "footer_text": "Designing with clarity, consistency, and care.",
                "header_cta_text": "Lets chat",
                "header_cta_target": "#contact",
                "about_intro": "Creative and detail-oriented Social Media Manager and Content Designer. Skilled in Canva, CapCut, and cross-platform scheduling. Currently finishing a B.Sc. in Computer Science and Engineering with research in AI-assisted patient referral systems.",
                "services_intro": "Social media design, content planning, brand visuals, and scheduling for growing businesses.",
                "skills_intro": "Design tools, social strategy, and production workflows used to deliver fast, consistent content.",
                "work_intro": "A mix of social media designs, marketing visuals, and brand content.",
                "experience_intro": "Experience across agencies and remote teams delivering content at scale.",
                "contact_intro": "Reach out for social media design, content calendars, and branding visuals.",
                "features_intro": "Reliable delivery, consistent brand style, and hands-on social publishing.",
            },
        )

        if created:
            self.stdout.write(self.style.SUCCESS("Created SiteProfile demo content."))

        if not AboutCard.objects.exists():
            AboutCard.objects.bulk_create(
                [
                    AboutCard(
                        title="B.Sc. in Computer Science and Engineering",
                        body="World University of Bangladesh. CGPA 3.64 / 4.00 (final semester, 138/148 credits).",
                        order=0,
                    ),
                    AboutCard(
                        title="Higher Secondary Certificate (HSC)",
                        body="Uttara High School and College. Result 4.25 / 5.00.",
                        order=1,
                    ),
                    AboutCard(
                        title="Secondary School Certificate (SSC)",
                        body="Uttara High School and College. Result 4.06 / 5.00.",
                        order=2,
                    ),
                ]
            )
            self.stdout.write(self.style.SUCCESS("Seeded Education cards."))

        if not Service.objects.exists():
            Service.objects.bulk_create(
                [
                    Service(
                        title="Social Media Strategy and Scheduling",
                        body="Plan, design, and schedule content that matches brand tone and platform goals.",
                        order=0,
                    ),
                    Service(
                        title="Canva and Visual Design",
                        body="Carousel posts, banners, and marketing visuals with consistent brand style.",
                        order=1,
                    ),
                    Service(
                        title="CapCut Video Editing",
                        body="Short-form reels, edits, and pacing optimized for engagement.",
                        order=2,
                    ),
                    Service(
                        title="Content Calendar Planning",
                        body="Weekly and monthly content planning with templates and workflow support.",
                        order=3,
                    ),
                ]
            )
            self.stdout.write(self.style.SUCCESS("Seeded Services."))

        if not Highlight.objects.exists():
            Highlight.objects.bulk_create(
                [
                    Highlight(value="147", label="Visual assets delivered in 1 month", order=0),
                    Highlight(value="110+", label="Hours worked in one month", order=1),
                    Highlight(value="20+", label="Extra hours to meet deadlines", order=2),
                    Highlight(value="3.64", label="CGPA", order=3),
                ]
            )
            self.stdout.write(self.style.SUCCESS("Seeded Highlights."))

        if not Feature.objects.exists():
            Feature.objects.bulk_create(
                [
                    Feature(
                        title="High-volume delivery",
                        body="Delivered 147 assets in a single month across posts, reels, and graphics.",
                        order=0,
                    ),
                    Feature(
                        title="Reliable scheduling",
                        body="Publishing rights on Meta and cross-platform scheduling experience.",
                        order=1,
                    ),
                    Feature(
                        title="Content consistency",
                        body="Brand-aligned visuals with strong storytelling and consistent tone.",
                        order=2,
                    ),
                    Feature(
                        title="AI-assisted workflows",
                        body="Used AI tools to plan and streamline content workflows.",
                        order=3,
                    ),
                ]
            )
            self.stdout.write(self.style.SUCCESS("Seeded Features."))

        if not SocialLink.objects.exists():
            SocialLink.objects.create(
                url="https://linkedin.com/in/iqrayeafhyira/",
                order=0,
            )
            self.stdout.write(self.style.SUCCESS("Seeded Social links."))

        if not Skill.objects.exists():
            Skill.objects.bulk_create(
                [
                    Skill(name="Social Media Strategy and Scheduling", proficiency="Advanced"),
                    Skill(name="Canva and Visual Design", proficiency="Advanced"),
                    Skill(name="CapCut Video Editing", proficiency="Advanced"),
                    Skill(name="Meta Business Suite", proficiency="Intermediate"),
                    Skill(name="AI Assisted Content Workflow", proficiency="Intermediate"),
                    Skill(name="Content Calendar Planning", proficiency="Advanced"),
                    Skill(name="MS and Google Office Suite", proficiency="Intermediate"),
                ]
            )
            self.stdout.write(self.style.SUCCESS("Seeded Skills."))

        if not Experience.objects.exists():
            Experience.objects.bulk_create(
                [
                    Experience(
                        job_title="Social Media and Content Manager (Promoted)",
                        company="Call The Cleaners, Australia - Remote",
                        start_date="2025-08-01",
                        end_date=None,
                        description="Promoted from part-time designer to full-time Social Media Manager. Responsible for designing, scheduling, and publishing posts and reels with publishing rights on Meta.",
                    ),
                    Experience(
                        job_title="Social Media Content Creator and Designer",
                        company="ElitSpire, Australia - Remote",
                        start_date="2024-01-01",
                        end_date="2025-08-01",
                        description="Designed posts and reels, created marketing visuals, and scheduled content across social platforms.",
                    ),
                    Experience(
                        job_title="Social Media and Creative Designer",
                        company="360 Photo Booth BD",
                        start_date="2023-01-01",
                        end_date="2024-01-01",
                        description="Transformed older content themes into new designs, reels, and static posts aligned with brand tone.",
                    ),
                    Experience(
                        job_title="Social Media Assistant",
                        company="TiqBud - Dhaka, Bangladesh",
                        start_date="2022-08-01",
                        end_date="2023-01-01",
                        description="Managed creative production and ensured engaging content. Increased organic reach via reels and Canva graphics.",
                    ),
                    Experience(
                        job_title="Graphics Designer (Volunteer)",
                        company="WUBCS",
                        start_date="2022-01-01",
                        end_date="2023-01-01",
                        description="Designed posters, banners, and event visuals for university tech events and promotions.",
                    ),
                ]
            )
            self.stdout.write(self.style.SUCCESS("Seeded Experience."))

        if not Project.objects.exists():
            Project.objects.bulk_create(
                [
                    Project(
                        title="International Client Social Pack",
                        description="High-volume social kit with posts, reels, graphics, and banners.",
                        category="Social Design",
                        url="https://behance.net",
                    ),
                    Project(
                        title="Brand Visual Refresh",
                        description="Modern templates and visuals aligned to brand tone and consistency.",
                        category="Branding",
                        url="https://behance.net",
                    ),
                    Project(
                        title="Marketing Visual Series",
                        description="Promotional posts and visuals for campaigns and offers.",
                        category="Marketing",
                        url="https://behance.net",
                    ),
                    Project(
                        title="Event Posters and Banners",
                        description="Posters and event visuals created for university programs.",
                        category="Print",
                        url="https://behance.net",
                    ),
                ]
            )
            self.stdout.write(self.style.SUCCESS("Seeded Projects."))

        self.stdout.write(self.style.SUCCESS("Demo data seeding complete."))
